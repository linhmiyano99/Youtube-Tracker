import csv
import os
from datetime import datetime

import requests
import time

from secret import API_KEY

# thông tin video
VIDEO_ID = "KB6W-BDBL5s"

# hàm lấy thống kê

def get_video_stats(video_id):
    print(API_KEY)
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "part": "statistics",
        "id": video_id,
        "key": API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    stats = data["items"][0]["statistics"]
    return {
        "viewCount": stats.get("viewCount", 0),
        "likeCount": stats.get("likeCount", 0),
        "commentCount": stats.get("commentCount", 0)
    }

while True:
    try:
        today = datetime.now().strftime("%Y-%m-%d")
        filename = f"stats_KB6W-BDBL5s_{today}.csv"
        file_exists = os.path.isfile(filename)

        stats = get_video_stats(VIDEO_ID)
        timestamp = datetime.now().isoformat()

        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                # nếu file mới, ghi header
                writer.writerow(["timestamp", "video_id", "viewCount", "likeCount", "commentCount"])
            writer.writerow([
                timestamp,
                VIDEO_ID,
                stats['viewCount'],
                stats['likeCount'],
                stats['commentCount']
            ])
        print(f"[{timestamp}] Saved to {filename}: view={stats['viewCount']}, like={stats['likeCount']}, comment={stats['commentCount']}")
    except Exception as e:
        print("Error:", e)
    time.sleep(60)