#!/usr/bin/env python3
import os, sqlite3, subprocess, json
from pathlib import Path
import yt_dlp
from tqdm import tqdm
import scenedetect
from scenedetect import VideoManager, SceneManager
from scenedetect.detectors import ContentDetector
from dotenv import load_dotenv
import google.generativeai as genai
import faiss
import numpy as np

# -------------------------------
# Load API
# -------------------------------
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro")

# -------------------------------
# Paths
# -------------------------------
BASE_DIR = Path("playlists")
BASE_DIR.mkdir(exist_ok=True)
DB_PATH = BASE_DIR / "ytai.db"
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# -------------------------------
# Database Schema
# -------------------------------
cur.executescript("""
CREATE TABLE IF NOT EXISTS playlists(id TEXT PRIMARY KEY, title TEXT);
CREATE TABLE IF NOT EXISTS videos(id TEXT PRIMARY KEY, playlist_id TEXT, title TEXT, description TEXT, views INTEGER, likes INTEGER, uploader TEXT, upload_date TEXT);
CREATE TABLE IF NOT EXISTS clips(video_id TEXT, clip_path TEXT, start_time REAL, end_time REAL, engagement_score REAL);
CREATE TABLE IF NOT EXISTS ai_analysis(video_id TEXT, hook_analysis TEXT, viral_strategy TEXT, title_ideas TEXT, description_ideas TEXT, sentiment_score REAL);
CREATE TABLE IF NOT EXISTS scenes(video_id TEXT, start_time REAL, end_time REAL, clip_path TEXT);
CREATE TABLE IF NOT EXISTS subtitles(video_id TEXT, subtitle_text TEXT);
CREATE TABLE IF NOT EXISTS embeddings(video_id TEXT, vector BLOB);
""")
conn.commit()

# -------------------------------
# Downloader
# -------------------------------
def download_playlist(url):
    ydl_opts = {
        "format": "bestvideo[height=1080]+bestaudio/best[height=1080]/best",
        "merge_output_format": "mp4",
        "writethumbnail": True,
        "writesubtitles": True,
        "writeautomaticsub": True,
        "outtmpl": "%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s",
        "quiet": True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        playlist_title = info.get("title", "playlist")
        playlist_id = info.get("id")
        cur.execute("INSERT OR IGNORE INTO playlists VALUES (?,?)",(playlist_id, playlist_title))
        conn.commit()
        for entry in info["entries"]:
            if not entry: continue
            video_meta = {
                "id": entry.get("id"),
                "title": entry.get("title"),
                "description": entry.get("description"),
                "views": entry.get("view_count"),
                "likes": entry.get("like_count"),
                "uploader": entry.get("uploader"),
                "upload_date": entry.get("upload_date")
            }
            cur.execute("""
                INSERT OR REPLACE INTO videos
                VALUES (?,?,?,?,?,?,?,?)
            """, (
                video_meta["id"], playlist_id, video_meta["title"], video_meta["description"],
                video_meta["views"], video_meta["likes"], video_meta["uploader"], video_meta["upload_date"]
            ))
            conn.commit()
    print(f"Downloaded playlist: {playlist_title}")

# -------------------------------
# Scene Detection + Clip Extraction
# -------------------------------
def detect_and_chop(video_path, video_id):
    video_manager = VideoManager([str(video_path)])
    scene_manager = SceneManager()
    scene_manager.add_detector(ContentDetector(threshold=30.0))
    video_manager.set_downscale_factor(1)
    video_manager.start()
    scene_manager.detect_scenes(frame_source=video_manager)
    scene_list = scene_manager.get_scene_list()
    clips_dir = video_path.parent / f"{video_id}_scenes"
    clips_dir.mkdir(exist_ok=True)
    for i, (start, end) in enumerate(tqdm(scene_list, desc="Chopping Scenes")):
        start_seconds, end_seconds = start.get_seconds(), end.get_seconds()
        clip_file = clips_dir / f"{video_id}_scene_{i+1}.mp4"
        subprocess.run(["ffmpeg","-y","-i",str(video_path),"-ss",str(start_seconds),"-to",str(end_seconds),"-c","copy",str(clip_file)])
        cur.execute("INSERT INTO scenes VALUES (?,?,?,?)",(video_id, start_seconds, end_seconds, str(clip_file)))
    conn.commit()

# -------------------------------
# AI Analysis
# -------------------------------
def analyze_video(video_meta):
    prompt = f"""
Analyze this YouTube video metadata.
Title: {video_meta['title']}
Description: {video_meta['description']}
Views: {video_meta['views']}
Likes: {video_meta['likes']}
Uploader: {video_meta['uploader']}
Provide:
- Hook analysis
- Emotional tone
- Content strategy
- Viral title & description drafts
"""
    response = model.generate_content(prompt)
    analysis = response.text.strip()
    cur.execute("INSERT INTO ai_analysis VALUES (?,?,?,?,?,?,?)",
                (video_meta['id'], analysis, analysis, analysis, analysis, 0.0, 0.0))
    conn.commit()
    return analysis

# -------------------------------
# Embeddings
# -------------------------------
def generate_embedding(text, video_id):
    vector = np.random.rand(768).astype('float32')  # placeholder for actual embeddings
    cur.execute("INSERT OR REPLACE INTO embeddings VALUES (?,?)",(video_id, vector.tobytes()))
    conn.commit()
    return vector

# -------------------------------
# CLI Main
# -------------------------------
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["download","analyze","scenes","clips"])
    parser.add_argument("--url", help="Playlist URL")
    args = parser.parse_args()

    if args.command=="download":
        download_playlist(args.url)
    elif args.command=="analyze":
        cur.execute("SELECT * FROM videos")
        for row in cur.fetchall():
            video_meta = {"id":row[0],"title":row[2],"description":row[3],"views":row[4],"likes":row[5],"uploader":row[6]}
            analyze_video(video_meta)
            generate_embedding(video_meta["title"]+video_meta["description"], video_meta["id"])
    elif args.command=="scenes":
        cur.execute("SELECT id,title FROM videos")
        for vid_id,title in cur.fetchall():
            video_file = Path(f"{title}/{title}.mp4")
            if video_file.exists():
                detect_and_chop(video_file, vid_id)
