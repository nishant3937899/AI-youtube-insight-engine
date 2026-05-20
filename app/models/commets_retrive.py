import pandas as pd
from googleapiclient.discovery import build

API_KEY = 'AIzaSyDmH1-R0RSWrNpehkezzc1YS6N5CynulAU'  

def get_comments(vid_id:str):
    url = vid_id

    video_id = url.split("=")[1]

    print(video_id)
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    
    comments_list = []
    
    
    request = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    maxResults=100, 
    textFormat="plainText"
    )
    
    print(f"Fetching comments for video: {video_id}...")
    
    comments_list=[]
    for i in range(5):
        response=request.execute()
    
        for item in response['items']:
            comment_data=item['snippet']['topLevelComment']['snippet']

            comments_list.append({
                'Comment': comment_data['textDisplay']

            })

    df=pd.DataFrame(comments_list)

    return df