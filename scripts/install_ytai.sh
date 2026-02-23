#!/data/data/com.termux/files/usr/bin/bash
pkg update -y
pkg install python ffmpeg git -y
pip install yt-dlp google-generativeai scenedetect[opencv] tqdm python-dotenv faiss-cpu
mkdir -p $PREFIX/bin
pip install reqs
curl -L -o ytai.py https://github.com/Media-CLis/YTAI-CLi/raw/refs/heads/main/cli/ytai.py
chmod +x ytai.py
reqs . > requirements.txt 
pip install -r requirements.txt 
rm requirements.txt 
mv ytai.py $PREFIX/bin/ytai
echo "YTAI installed. Run with: ytai download --url <playlist_url>"
