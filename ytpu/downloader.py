# downloader.py

import subprocess
import json


def get_playlist_info(url) -> dict:
    cmd = ["yt-dlp", "--flat-playlist", "-J", url]
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Error in request {url} due to {result.stderr}")
        quit()

    try:
        return json.loads(result.stdout)
    except Exception as e:
        print(f"Failed to convert to JSON due to {e}")
        quit()
