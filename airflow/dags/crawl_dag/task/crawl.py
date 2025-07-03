import os
import time
from datetime import datetime
import requests
from pymongo import MongoClient
from crawl_dag.load_config import api_key, mongo_uri, VIDEO_ID


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
#
# while True:
#     try:
#         stats = get_video_stats(VIDEO_ID)
#         timestamp = datetime.now().isoformat()
#
#         # save to MongoDB
#         document = {
#             "timestamp": timestamp,
#             "video_id": VIDEO_ID,
#             "viewCount": stats['viewCount'],
#             "likeCount": stats['likeCount'],
#             "commentCount": stats['commentCount']
#         }
#         collection.insert_one(document)
#
#         print(
#             f"[{timestamp}] Saved to MongoDB: view={stats['viewCount']}, like={stats['likeCount']}, comment={stats['commentCount']}"
#         )
#     except Exception as e:
#         print("Error:", e)
#     time.sleep(60)
