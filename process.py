import warhouseservice
import harvestingservice

class mainprocess:
    def __init__(self, config):
        self.config = config
        self.hh = harvestingservice.harvestinghelper(self.config)
        self.wh = warhouseservice.warhousehelper(self.config)

    def harvesting(self, channel_id):
        print("Processing...")

        data = self.hh.getdatabychannelid(channel_id)
        if data == None:
            self.hh.insertmongoprocess(channel_id)
        else:
            self.hh.deletedatabychannelid(channel_id)
            print("Channel data is already available, so we are deleting the data and harvesting again")
            self.hh.insertmongoprocess(channel_id)

        print("Harvesting completed for this channel Channel Id : " + channel_id)

    def warhousing(self, channel_name):
        print("Processing...")

        mongodata = self.hh.getdatabychannelname(channel_name)
        channel_id = ""
        if mongodata != None:
            channel_id = mongodata["Channel_Name"]["channel_id"]
            print(channel_id)
            sqlchanneldata = self.wh.getChannelDatabychannelId(channel_id)
            if len(sqlchanneldata) == 0:
                self.wh.insertChannelData(mongodata)
            else:
                self.wh.deleteChannelDatabychannelId(channel_id)
                print("Channel data is already available, so we are deleting the data and warhousing again")
                self.wh.insertChannelData(mongodata)

            print("Warhousing completed for this channel Channel Id : " + channel_id)
        else:
            print("No data is available to Migrate for this channel name : " + channel_name)
    
    def getChannelDatabychannelId(self, channel_Id):
        return self.wh.getChannelDatabychannelId(channel_Id) 
    
    def getListofHarvestedChannels(self):
        return self.hh.getlisofharvestedchannel() 

    def getListofChannels(self, channel_Id):
        return self.wh.getListofChannels(channel_Id) 

    def getListofChannelDetails(self, channel_Id, channel_name, video_name, video_description):
        return self.wh.getListofChannelDetails(channel_Id, channel_name, video_name, video_description) 
    
    def getQA(self, QuestionType, channel_Id):
        return self.wh.getQA(QuestionType, channel_Id)
