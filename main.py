import process

class mainfunction:
    def __init__(self):
        config = {
            "api_key" : 'AIzaSyAqkMyd-Dp5gB3pxc7OU3TeFgBxaRnQoHY',
            "sqlconn" : "Driver={SQL Server Native Client 11.0};Server=BOOBESH\SQLEXPRESS;Database=Youtube;uid=sa;pwd=123",
            "mongoconn" : "mongodb://localhost:27017/",
            "mongodbname" : "YouTubeData",
            "mongodbcolname" : "ChannelData"
        }
        self.mp = process.mainprocess(config)

    def executeharvesting(self, channel_id):
        self.mp.harvesting(channel_id)

    def executewarhousing(self, channel_name):
        self.mp.warhousing(channel_name)
    
    def getListofHarvestedChannels(self):
        return self.mp.getListofHarvestedChannels() 

    def getChannelDatabychannelId(self, channel_Id):
        return self.mp.getChannelDatabychannelId(channel_Id) 
    
    def getListofChannels(self, channel_Id):
        return self.mp.getListofChannels(channel_Id) 

    def getListofChannelDetails(self, channel_Id, channel_name, video_name, video_description):
        return self.mp.getListofChannelDetails(channel_Id, channel_name, video_name, video_description) 
    
    def getQA(self, QuestionType, channel_Id):
        return self.mp.getQA(QuestionType, channel_Id)
