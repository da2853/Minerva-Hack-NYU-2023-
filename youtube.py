from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#DEVELOPER_KEY =
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def search_videos_by_keywords(keywords):
    print("keywords that have been given to me are:")
    print(keywords)
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    try:
        # Call the search.list method to retrieve search results
        search_response = youtube.search().list(
            q=keywords,
            type="video",
            part="id,snippet",
            maxResults=10  # Change this to the desired number of search results
        ).execute()

        videos = []
        # Process the search results
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                videos.append("https://www.youtube.com/watch?v=" + search_result["id"]["videoId"])
                # videos.append({
                #     #"title": search_result["snippet"]["title"],
                #     "video_id": "https://www.youtube.com/watch?v=" + search_result["id"]["videoId"],
                #     #"thumbnail_url": search_result["snippet"]["thumbnails"]["default"]["url"]
                # })

        return videos

    except HttpError as e:
        print("An error occurred: %s" % e)
        return None

#
# keywords = ['calculus', 'kids']
# videos = search_videos_by_keywords(keywords)
# for i in videos:
#     print(i)