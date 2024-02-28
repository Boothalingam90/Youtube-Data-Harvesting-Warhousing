import sqlconn
import streamlit as st

class warhousehelper:
    def __init__(self, config):
        self.sqlcon = sqlconn.sql(config["sqlconn"])

    def getchannelquery(self, data):
        return "channel_insert  @channel_id = ?, @channel_name = ?, @channel_type = ?, @channel_views = ?, @channel_description = ?, @channel_status = ?"

    def getchannelvalues(self, data):
        return (data["channel_id"], data["channel_name"], data["channel_type"],  data["channel_views"], data["channel_status"], data["channel_status"])

    def getplaylistquery(self, data):
        return "playlist_insert  @playlist_id = ?, @channel_id = ?, @playlist_name = ?"

    def getplaylistvalues(self, data):
        return (data["channel_playlists"], data["channel_id"], data["channel_name"])

    def getvideoquery(self, data):
        return "video_insert @video_id = ?, @playlist_id = ?, @video_name = ?, @video_description = ?, @published_date = ?, @view_count = ?, @like_count = ?, @dislike_count = ?, @favorite_count = ?, @comment_count = ?, @duration = ?, @thumbnail = ?, @caption_status = ?, @durationtime = ?"

    def getvideovalues(self, data):
        Video_Description = data["Video_Description"].encode("utf-8")
        # Video_Description = Video_Description[:10]
        return (data["Video_Id"], data["Playlist_id"], data["Video_Name"], Video_Description, data["PublishedAt"], data["View_Count"], data["Like_Count"], data["Dislike_Count"], data["Favorite_Count"], data["Comment_Count"], data["Duration"], data["Thumbnail"], data["Caption_Status"], data["TimeStamp"])
    
    def insertchannel(self, data):
        self.sqlcon.insert(self.getchannelquery(data), self.getchannelvalues(data))

    def insertplaylist(self, data):
        self.sqlcon.insert(self.getplaylistquery(data), self.getplaylistvalues(data))

    def insertvideo(self, data):
        self.sqlcon.insert(self.getvideoquery(data), self.getvideovalues(data))

    def insertcomment(self, data):
        comment_data = data["Comments"]
        insert_query = "comment_insert @comment_id = ?, @video_id = ?, @comment_text = ?, @comment_author = ?, @comment_published_date = ?, @like_count = ?, @reply_count = ?, @comment_key = ?"
        for commentitem in comment_data.keys():
            comment_tem_data = comment_data[commentitem]
            Comment_Text = comment_tem_data["Comment_Text"].encode("utf-8")
            # Comment_Text = Comment_Text[:10]
            commentvalues = (comment_tem_data["Comment_Id"], comment_tem_data["Video_Id"], Comment_Text, comment_tem_data["Comment_Author"], comment_tem_data["Comment_PublishedAt"], comment_tem_data["Like_count"], comment_tem_data["Reply_count"], comment_tem_data["Comment_key"])
            self.sqlcon.insert(insert_query, commentvalues)
    
    def insertChannelData(self, data):
        for item in data.keys():
            if item == "Channel_Name":
                self.insertchannel(data["Channel_Name"])
                self.insertplaylist(data["Channel_Name"])
            elif "Video_Id" in item:
                self.insertvideo(data[item])
                self.insertcomment(data[item])

    def deleteChannelDatabychannelId(self, channel_Id):
        return self.sqlcon.delete("DECLARE @channel_id VARCHAR(255) = '"+ channel_Id +"', @playlist_id VARCHAR(255); SELECT @playlist_id = playlist_id FROM dbo.Playlist WHERE channel_id = @channel_id;DELETE dbo.Comment WHERE video_id in (SELECT video_id FROM dbo.Videos(NOLOCK) WHERE Playlist_id = @playlist_id);DELETE dbo.Videos WHERE playlist_id = @playlist_id; DELETE dbo.Playlist WHERE playlist_id = @playlist_id;DELETE dbo.Channel WHERE channel_id = @channel_id;")  
    
    def getChannelDatabychannelId(self, channel_Id):
        return self.sqlcon.execute("EXEC dbo.getChannelData @Type = ?, @channel_id = ?", ('CDD', channel_Id)) 
    
    def getListofChannels(self, channel_Id):
        return self.sqlcon.execute("EXEC dbo.getChannelData @Type = ?, @channel_id = ?", ('CDA', channel_Id)) 

    def getListofChannelDetails(self, channel_Id, channel_name, video_name, video_description):
        return self.sqlcon.execute("EXEC dbo.getChannelData @Type = ?, @channel_id = ?, @channel_name = ?, @video_name = ?, @video_description = ?", ('LD', channel_Id, channel_name, video_name, video_description)) 
    
    def getQA(self, QuestionType, channel_Id):
        return self.sqlcon.execute("EXEC dbo.getChannelData @Type = ?, @channel_id = ?", (QuestionType, channel_Id))
            
       