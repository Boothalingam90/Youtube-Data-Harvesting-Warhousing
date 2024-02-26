import main

mf = main.mainfunction()
# channelIds = ['UCJcCB-QYPIBcbKcBQOTwhiA','UCnC8SAZzQiBGYVSKZ_S3y4Q','UCBHyHIpO3MzU8fiNM3FbFcA','UCYuQwKOCk8hipEa6uRhyHGQ',
#               'UCJhWD-Sy_VDbzxFvFJJE_Hw','UCs5rmLvEzb-AVKSXM3oO8Zg','UCs5rmLvEzb-AVKSXM3oO8Zg', 'UCgf2bJZYZ6JG9ObTfKwAS_A']

channelIds = ['UCgf2bJZYZ6JG9ObTfKwAS_A', 'UCsVLwAo9-qB3MIU18J7nJSg', 'UCB53hX_kvPKTYxbxiUhBHXA', 'UC38tpGV1AydcEOMomOgNwNA',
'UCOUuAcAMArRoy6k6zJ3uAxQ', 'UCOJfVamQGGG-eSrf1AqzMOQ', 'UCQjt8LFjuRt6sRLWFWLGMyw']

# channelIds = ['UCgf2bJZYZ6JG9ObTfKwAS_A']

# for item in channelIds:
#     mf.executeharvesting(item)
#     mf.executewarhousing(item)
    
userInput = input("Enter Type : ")
if userInput == "1" : # harvesting
    mf.executeharvesting(input("Enter Channel Id for harvesting : "))
elif userInput == "2" : # warhousing
    mf.executewarhousing(input("Enter Channel name for warhousing : "))
elif userInput == "3" : # Channel Data by channelId
    print(mf.getChannelDatabychannelId(input("Enter Channel Id to get Channel Data : ")))
elif userInput == "4" : # List of Channels
    print(mf.getListofChannels(""))
elif userInput == "5" : # List of Channel Details
    channel_Id = input("Enter Channel Id to filter : ");
    channel_name = input("Enter Channel name to filter : ");
    video_name = input("Enter video name to filter : ");
    video_description = input("Enter video description to filter : ");
    print(mf.getListofChannelDetails(channel_Id, channel_name, video_name, video_description))
elif userInput == "6" : # QA
    print(mf.getQA(input("Enter Question Type : "), ""))
