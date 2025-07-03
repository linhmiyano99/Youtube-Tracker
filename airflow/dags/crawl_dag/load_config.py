from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
mongo_uri = os.getenv("MONGO_URI")
VIDEO_ID = os.getenv("VIDEO_ID")
