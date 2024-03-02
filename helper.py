import pprint
import youtube
import common
import re
pp = pprint.PrettyPrinter(indent=4)

class helperClass:
    def __init__(self):
        self.cf = common.commonfunctions()

    def getChannelData(self, api_key, channel_id):
        yh = youtube.youtubeHarvesting(api_key)
        channel_object = {}
        channel_data = yh.getChannelDatabyChannelId(channel_id)    
        if len(channel_data) > 0:
            channel_data_items = self.cf.getValuesfromDictionary(channel_data, "items") 
            if len(channel_data_items) > 0:
                channel_informations = self.processChannelData(channel_data_items, channel_id)
                channel_object["Channel_Name"] = channel_informations
                self.processPlaylistData(yh, channel_object, "")

        return channel_object
    
    def processChannelData(self, channel_data_items, channel_id):
        return self.evaluateChannelData(channel_data_items[0], channel_id)

    def evaluateChannelData(self, data, channel_id):
        channel_informations = {
              'channel_id' : channel_id,
              'channel_name' : self.cf.getValuesfromDictionary(data, "snippet,title"),
              'channel_type' : "",
              'channel_views' : self.cf.getValuesfromDictionary(data, "statistics,viewCount"),
              'channel_description' :  self.cf.getValuesfromDictionary(data, "snippet,description"),
              'channel_status' : "",
              'channel_playlists' : self.cf.getValuesfromDictionary(data, "contentDetails,relatedPlaylists,uploads"),
              'channel_subscribers' : self.cf.getValuesfromDictionary(data, "statistics,subscriberCount"),
              'channel_videos' : self.cf.getValuesfromDictionary(data, "statistics,videoCount")
            } 
        return channel_informations 

    def processPlaylistData(self, yh, channel_object, pagetoken):
        playlist_id = channel_object["Channel_Name"]["channel_playlists"]

        playlist_data = yh.getPlaylistItemsbyPlaylistId(playlist_id, pagetoken)
        if len(playlist_data) > 0:

            nextPageToken = self.cf.getValuesfromDictionary(playlist_data, "nextPageToken")
            playlist_data_items = self.cf.getValuesfromDictionary(playlist_data, "items")
            if len(playlist_data_items) > 0:
                self.evaluatePlaylistData(yh, channel_object, playlist_id, playlist_data_items)
            
                if nextPageToken != "":
                    self.processPlaylistData(yh, channel_object, nextPageToken)

    def evaluatePlaylistData(self, yh, channel_object, playlist_id, data):
        return self.processVideoData(yh, channel_object, playlist_id, data)     

    def processVideoData(self, yh, channel_object, playlist_id, data):
        for item in data:
            video_id = self.cf.getValuesfromDictionary(item, "snippet,resourceId,videoId")
            video_position = self.cf.getValuesfromDictionary(item, "snippet,position")
            video_key = "Video_Id_" + str(video_position + 1)

            video_data = yh.getVideosbyVideoId(video_id)
            if len(video_data) > 0:
                video_data_items = self.cf.getValuesfromDictionary(video_data, "items")[0]

                if len(video_data_items) > 0:        
                    video_informations = self.evaluateVideoData(video_data_items, playlist_id)

                    self.processPagewiseCommentsData(yh, video_id, video_informations, "", 1)
                    channel_object[video_key] = video_informations

        return channel_object
    
    def evaluateVideoData(self, data, playlist_id):
        video_informations = {
            "Playlist_id": playlist_id,
            "Video_Id": self.cf.getValuesfromDictionary(data, "id"),
            "Video_Name": self.cf.getValuesfromDictionary(data, "snippet,title"),
            "Video_Description": self.cf.getValuesfromDictionary(data, "snippet,description"),
            "Tags": self.cf.getValuesfromDictionary(data, "snippet,tags"),
            "PublishedAt": self.cf.getValuesfromDictionary(data, "snippet,publishedAt"),
            "View_Count": self.cf.getValuesfromDictionary(data, "statistics,viewCount"),
            "Like_Count": self.cf.getValuesfromDictionary(data, "statistics,likeCount"),
            "Dislike_Count": 0,
            "Favorite_Count": self.cf.getValuesfromDictionary(data, "statistics,favoriteCount"),
            "Comment_Count": self.cf.getValuesfromDictionary(data, "statistics,commentCount"),
            "Duration": self.cf.getValuesfromDictionary(data, "contentDetails,duration"),
            "TimeStamp" : self.getDuration(self.cf.getValuesfromDictionary(data, "contentDetails,duration")),
            "Thumbnail": self.cf.getValuesfromDictionary(data, "contentDetails,definition"),
            "Caption_Status": self.cf.getValuesfromDictionary(data, "contentDetails,caption"),
            "Comments": {}
        }
        # print(video_informations)
        return video_informations

    def processPagewiseCommentsData(self, yh, video_id, video_informations, pagetoken, commentCount):
        comments_data = yh.getCommentsbyVideoId(video_id, pagetoken)
        if len(comments_data) > 0:
            nextPageToken = self.cf.getValuesfromDictionary(comments_data, "nextPageToken")

            commentCount = self.processCommentsData(comments_data, video_informations, commentCount)

            if nextPageToken != "":
                self.processPagewiseCommentsData(yh, video_id, video_informations, nextPageToken, commentCount + 1)

    def processCommentsData(self, data, video_informations, commentCount):
        comments_data_items = self.cf.getValuesfromDictionary(data, "items")
        if len(comments_data_items) > 0:
            for commentitem in comments_data_items:
                comment_key = "Comment_Id_" + str(commentCount) 
                video_informations["Comments"][comment_key] = self.evaluateCommentData(commentitem, comment_key)
                commentCount = commentCount + 1
        return commentCount
    
    def evaluateCommentData(self, data, comment_key):  
        comment_informations = {
            "Video_Id": self.cf.getValuesfromDictionary(data, "snippet,videoId"),
            "Comment_Id": self.cf.getValuesfromDictionary(data, "snippet,topLevelComment,id"),
            "Comment_Text": self.cf.getValuesfromDictionary(data, "snippet,topLevelComment,snippet,textDisplay"),
            "Comment_Author": self.cf.getValuesfromDictionary(data, "snippet,topLevelComment,snippet,authorDisplayName"),
            "Comment_PublishedAt": self.cf.getValuesfromDictionary(data, "snippet,topLevelComment,snippet,publishedAt"),
            "Like_count" : self.cf.getValuesfromDictionary(data, "snippet,topLevelComment,snippet,likeCount"),
            "Reply_count" : self.cf.getValuesfromDictionary(data, "snippet,totalReplyCount"),
            "Comment_key" : comment_key,
        }
        return comment_informations

    def getDuration(self, duration):
        if duration == "P0D":
            duration = "PT00H00M00S"

        match = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", duration)
        hours = int(match.group(1) or 0)
        minutes = int(match.group(2) or 0)
        seconds = int(match.group(3) or 0)
        strduration = str(hours) + ":" + str(minutes) + ":" + str(seconds)
        return strduration