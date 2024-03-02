import helper
hc = helper.helperClass()
import mongoconn

class harvestinghelper:
    def __init__(self, config):
        self.mongocon = mongoconn.mongo(config["mongoconn"], config["mongodbname"])
        self.mongodbcolname = config["mongodbcolname"]
        self.api_key = config["api_key"]

    def insertmongoprocess(self, channel_id):
        data = hc.getChannelData(self.api_key, channel_id)
        id = ""
        if len(data) > 0:
            self.mongocon.insert_one(self.mongodbcolname, data)
            id = channel_id
        return id
        
    def getdatabychannelid(self, channel_id):
        return self.mongocon.get_one(self.mongodbcolname, { "Channel_Name.channel_id" : channel_id })
    
    def getdatabychannelname(self, channel_name):
        return self.mongocon.get_one(self.mongodbcolname, { "Channel_Name.channel_name" : channel_name })
    
    def getlisofharvestedchannel(self):
        data = self.mongocon.get(self.mongodbcolname, {})
        channels = []
        for item in data:
            channels.append(item["Channel_Name"]["channel_name"])
        return channels

    def deletedatabychannelid(self, channel_id):
        return self.mongocon.del_one(self.mongodbcolname, { "Channel_Name.channel_id" : channel_id })

            
       