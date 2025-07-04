import os
import time
from datetime import datetime
import requests
from crawl_dag.load_config import api_key, VIDEO_ID


# connect to MongoDB
# client = MongoClient(mongo_uri)
# db = client["youtube_stats"]
# collection = db["video_statistics"]
def get_video_stats(video_id):
    print("api_key", api_key)

    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "part": "statistics",
        "id": video_id,
        "key": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    print("data", data)
    stats = data["items"][0]["statistics"]
    return {
        "viewCount": int(stats.get("viewCount", 0)),
        "likeCount": int(stats.get("likeCount", 0)),
        "commentCount": int(stats.get("commentCount", 0))
    }
