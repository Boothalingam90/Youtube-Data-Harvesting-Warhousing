from googleapiclient.discovery import build

class youtubeHarvesting:
    def __init__(self, api_key):        
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey = self.api_key)
        
    def getChannelDatabyChannelId(self, channel_id):
        try:
            channel_response = self.youtube.channels().list(
            id = channel_id,
            part ='snippet,statistics,contentDetails,status',
            )
            return channel_response.execute()
        except Exception as error:
            # handle the exception
            print("An exception occurred while fetching channel : ", error)
        return ""
    
    def getPlaylistItemsbyPlaylistId(self, playlist_id, pageToken):
        try:
            playlist_request = self.youtube.playlistItems().list(
                playlistId = playlist_id,
                part = "snippet,contentDetails",
                maxResults = 50,
                pageToken = pageToken
            )
            return playlist_request.execute()
        except Exception as error:
            # handle the exception
            print("An exception occurred while fetching playlist : ", error)
        return ""
    
    def getVideosbyVideoId(self, video_id):
        try:
            video_request = self.youtube.videos().list(
                part = "snippet,contentDetails,statistics,topicDetails,status",
                id = video_id
            )
            return video_request.execute()
        except Exception as error:
            # handle the exception
            print("An exception occurred while fetching videos : ", error)
        return ""
    
    def getCommentsbyVideoId(self, video_id, pageToken):
        try:
            comments_request = self.youtube.commentThreads().list(
                part = "snippet,replies",
                videoId = video_id,
                maxResults = 100,
                pageToken = pageToken
            )
            return comments_request.execute()
        except Exception as error:
            # handle the exception
            print("An exception occurred while fetching comments : ", error)
        return ""