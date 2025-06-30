# Youtube-Tracker

add file: src/main/.env

``` 
API_KEY=...
MONGO_URI=mongodb://admin:admin@mongo:27017/
VIDEO_ID=bu39oUbbHxc
```

## GET API_KEY
Because every API_KEY is limited by 10000 calls/day 
=> You should create your own `API_KEY`

Follow 2 steps:
- Enable `YouTube Data API v3` https://console.cloud.google.com/marketplace/product/google/youtube.googleapis.com?q=search&referrer=search&inv=1&invt=Ab1a9A&project=primal-device-464206-j5
- Get `API_KEY` from https://console.cloud.google.com/apis/credentials?referrer=search&inv=1&invt=Ab1a9A&project=primal-device-464206-j5
