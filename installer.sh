curl -sL https://github.com/Media-CLis/YTAI-CLi/raw/refs/heads/main/scripts/install_ytai.sh | bash

cat << EOF

   !!!  DONE INSTALLING !!!

run:
		ytai download --url <playlist_url>


Commands

Command	                              \| Description
	ytai download --url <playlist>	      \| Download all videos in 1080p with metadata

	ytai analyze	                      \| Run Gemini AI viral analysis + embeddings

	ytai scenes	                          \| Auto detect scenes and chop videos

	ytai clips	                          \| Extract hook clips + AI-prioritized highlights

	ytai search <query>	                  \| Semantic search over all videos + clips

	ytai dashboard	                      \| Launch the FastAPI + React dashboard

EOF

