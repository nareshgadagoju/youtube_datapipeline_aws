import pandas as pd
import s3fs
from googleapiclient.discovery import build

def run_youtube_etl():

    # Replace 'YOUR_API_KEY' with your actual YouTube Data API key.
    api_key = 'YOUTUBE_API'

    # Initialize the YouTube Data API client.
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Specify the video ID for which you want to extract comments.
    video_id = 'VIDEO_ID'

    # Call the YouTube API to retrieve video comments.
    def get_video_comments(video_id):
        comments = []
        next_page_token = None  # Initialize the next page token

        while True:
            results = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                textFormat='plainText',
                pageToken=next_page_token  # Pass the next page token
            ).execute()

            for item in results['items']:
                comment = item['snippet']['topLevelComment']['snippet']
                username = comment['authorDisplayName']
                timestamp = comment['publishedAt']
                comments.append({
                    'Username': username,
                    'Timestamp': timestamp,
                    'Comment': comment['textDisplay']
                })
                next_page_token = results.get('nextPageToken')  # Get the next page token

            if not next_page_token:
                break  # No more pages to fetch

        return comments

    # Retrieve comments for the specified video.
    video_comments = get_video_comments(video_id)

    # Create a DataFrame from the comments
    df = pd.DataFrame(video_comments)

    # Save the data to a CSV file
    s3_path = 's3://BUCKET_NAME/youtube_comments.csv'  # Replace BUCKETNAME with your S3 bucket name
    df.to_csv(s3_path, index=False)