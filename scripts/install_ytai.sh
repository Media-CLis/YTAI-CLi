#!/data/data/com.termux/files/usr/bin/bash
pkg update -y
pkg install python ffmpeg git -y
pip install yt-dlp google-generativeai scenedetect[opencv] tqdm python-dotenv faiss-cpu
mkdir -p $PREFIX/bin

curl -L -o ytai.py https://github.com/Media-CLis/YTAI-CLi/raw/refs/heads/main/cli/ytai.py
chmod +x ytai.py
# Deep detect & generate full requirements
pip install req-scanner
req-scanner generate . --include-deps

# Smart detection with best import maps
pip install reqdev
reqdev generate . -o requirements.txt

# Detect + install in one shot
pip install requirements-installer
requirements-installer auto-install .
pip install -r requirements.txt 
rm requirements.txt 
mv ytai.py $PREFIX/bin/ytai
echo "YTAI installed. Run with: ytai download --url <playlist_url>"
