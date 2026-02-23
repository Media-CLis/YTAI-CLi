# YTAI-CLi
YTAI Media Intelligence Lab   **“Because watching 300 YouTube videos manually is so 2010.”**  

# 🎬 YTAI Media Intelligence Lab  
**“Because watching 300 YouTube videos manually is so 2010.”**  

![YTAI Logo Placeholder](https://via.placeholder.com/400x100?text=YTAI+Lab)

---

## 🚀 TL;DR

YTAI is basically **your personal AI-powered YouTube ninja**, built for developers who like:  

- Watching videos **without watching videos**  
- Extracting clips like a caffeinated video editor  
- Analyzing metadata until the pixels scream  
- Turning playlists into a **playground of insights**  
- Proving your friends that AI can binge faster than they can  

It downloads, chops, analyzes, scores, and even gives scene-by-scene viral advice — because who doesn’t want Gemini AI to roast or praise their favorite content creators?

---

## 🎯 Features (aka Why You’ll Love This Insane Tool)

- **1080p Downloader**: Only the finest pixels, none of that potato-resolution nonsense.  
- **Automated Scene Detection**: Cuts videos into digestible chunks like a sushi chef on Red Bull.  
- **Clip Extraction**: 30-second hooks, AI-highlighted segments, shorts-ready.  
- **Google Gemini AI Integration**: Generates viral titles, SEO descriptions, emotional tone analysis, and probably unsolicited opinions about your playlist choices.  
- **Subtitle Sentiment Analysis**: Find out if the speaker is happy, sad, or just faking it for views.  
- **SQLite + FAISS Search**: Semantic search over everything — because keyword search is for peasants.  
- **FastAPI + React Dashboard**: Browse clips, analyze engagement, and pretend you built Netflix.  
- **Automated Scheduler**: Runs while you sleep, drinks coffee, or stare at the ceiling.  
- **Dockerized & Termux Ready**: Run it anywhere, because why not?  

---

## 🧰 Tech Stack

- **Python** – duh  
- **yt-dlp + FFmpeg** – ripping, merging, chopping, pixel love  
- **PySceneDetect** – for making sense of cuts and transitions  
- **Google Gemini AI** – your brain, but faster and less judgmental  
- **SQLite + FAISS** – for storage and semantic wizardry  
- **FastAPI + React** – because web dashboards make devs feel fancy  
- **Docker** – so it can live anywhere without screaming dependencies  

---

## 🏗 Installation

### Termux one-liner:
curl https://github.com/Media-CLis/YTAI-CLi/raw/refs/heads/main/scripts/install_ytai.sh | bash
ytai download --url <playlist_url>
```
## ⚡ CLI Commands

| Command | Description |
|---------|-------------|
| `ytai download --url <playlist>` | Download all videos in 1080p with metadata |
| `ytai analyze` | Run Gemini AI viral analysis + embeddings |
| `ytai scenes` | Auto detect scenes and chop videos |
| `ytai clips` | Extract hook clips + AI-prioritized highlights |
| `ytai search <query>` | Semantic search over all videos + clips |
| `ytai dashboard` | Launch the FastAPI + React dashboard |

---

## 🧠 How it Works (Developer Edition)

1. `yt-dlp` fetches videos and metadata like a polite robot.  
2. Scene detection chops videos into tiny, analyzable chunks.  
3. Gemini AI whispers in your ear, “This clip will go viral, trust me.”  
4. Clips, scenes, and embeddings are stored in SQLite + FAISS for semantic search and research.  
5. FastAPI serves it all; React makes it look less like a CLI nightmare.  
6. You now appear to your team as the AI-powered content wizard.  

---

## 😎 Why You Need This

- Tired of manually analyzing videos for trends?  
- Want AI to roast your playlist or generate click-worthy titles?  
- Curious about sentiment per scene?  
- Want to impress coworkers with a shiny FastAPI dashboard?  

---

## ⚠️ Warning

- May cause severe addiction to analyzing video metadata.  
- Could result in you watching fewer videos… or too many, depending on AI clip output.  
- Gemini AI might start suggesting your own content strategy. Don’t say we didn’t warn you.  

---

## 🏁 Next Steps

- Add audio-based scene detection  
- Generate composite highlight reels  
- Auto-update playlists on a schedule  
- Optional: make the React dashboard flashy enough to distract coworkers 

---
## Folder Structure 
```
ytai_lab/
 ├── cli/
 │    └── ytai.py                 # Main CLI
 ├── db/
 │    └── ytai.db                  # SQLite DB
 ├── data/
 │    └── playlists/               # videos, clips, thumbnails
 ├── backend/
 │    ├── main.py                  # FastAPI server
 │    └── embeddings.py            # FAISS vector search
 ├── frontend/
 │    └── react_app/               # React dashboard scaffold
 ├── scripts/
 │    └── scheduler.py             # APScheduler jobs
 ├── Dockerfile                     # Full containerization
 └── .env                           # GEMINI_API_KEY
```


## React Frontend (Scaffold)
```
frontend/react_app/
 ├── package.json
 ├── src/
 │    ├── App.jsx      # fetch /videos, /clips and display
 │    └── components/
 │         ├── VideoList.jsx
 │         ├── ClipPlayer.jsx
 │         └── SearchBar.jsx
```
## 📝 License

MIT – Because sharing is caring, even if you’re stealing scenes from cat videos.
