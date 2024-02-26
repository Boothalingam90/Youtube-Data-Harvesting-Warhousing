import streamlit as st
import pandas as pd
import numpy as np
import main

config = {
            "api_key" : 'AIzaSyAqkMyd-Dp5gB3pxc7OU3TeFgBxaRnQoHY',
            # "sqlconn" : "Driver={SQL Server Native Client 11.0};Server=BOOBESH\SQLEXPRESS;Database=Youtube;uid=sa;pwd=123",
            "sqlconn" : st.secrets["sql_conn_string"],
            # "mongoconn" : "mongodb://localhost:27017/",
            "mongoconn" : "mongodb+srv://" + st.secrets["mongo_db_username"] + ":" + st.secrets["mongo_db_password"] + "@clustercapstoneyoutube.h0eq7on.mongodb.net/?retryWrites=true&w=majority&appName=ClusterCapstoneYoutube",
            "mongodbname" : "YouTubeData",
            "mongodbcolname" : "ChannelData"
        }
mf = main.mainfunction(config)

st.set_page_config("Youtube Data Harvesting and Warhousing")

st.header("Youtube Data Harvesting and Warhousing")

tab1, tab2, tab3, tab4 = st.tabs(["Search", "Harvesting", "Warhousing", "Questions"])

with tab1:
   SearchChannelName = st.text_input('Channel Name : ', '')
   SearchVideoName = st.text_input('Video Name : ', '')
   SearchDescription = st.text_input('Description : ', '')
   submitSearch = st.button("Search")
   if submitSearch:
    header = ["Video name", "Video description", "Published date", "View count", "Like count", "Channel name"]
    df = pd.DataFrame(mf.getListofChannelDetails("", SearchChannelName, SearchVideoName, SearchDescription), columns=(header))
    df.index = np.arange(1, len(df) + 1)
    st.dataframe(df)

with tab2:
   HarvestingChannelId = st.text_input('Channel Id : ', '')
   submitFetch = st.button("Fetch Channel Details")
   if submitFetch:
    st.info("Processing...")
    mf.executeharvesting(HarvestingChannelId)
    st.success("Harvesting completed for this channel")

with tab3:
   MigrateChannelname = st.selectbox('Please select Channel name : ', mf.getListofHarvestedChannels())
   submitMigrate = st.button("Migrate")
   if submitMigrate:
    st.info("Processing...")
    mf.executewarhousing(MigrateChannelname)
    st.success("Warhousing completed for this channel")

with tab4:
   QuestionsDetails = []
   QuestionsDetails.append({"question" : "1.What are the names of all the videos and their corresponding channels?", "id" : "Q1", "header" : ["Channel name", "Video name"]})
   QuestionsDetails.append({"question" : "2.Which channels have the most number of videos, and how many videos do they have?", "id" : "Q2", "header" : ["Channel name", "No. of Videos"]})
   QuestionsDetails.append({"question" : "3.What are the top 10 most viewed videos and their respective channels?", "id" : "Q3", "header" : ["Channel name", "Video name", "Most viewed videos"]})
   QuestionsDetails.append({"question" : "4.How many comments were made on each video, and what are their corresponding video names?", "id" : "Q4", "header" : ["Video name", "Comment count"]})
   QuestionsDetails.append({"question" : "5.Which videos have the highest number of likes, and what are their corresponding channel names?", "id" : "Q5", "header" : ["Channel name", "Video name", "Most liked videos"]})
   QuestionsDetails.append({"question" : "6.What is the total number of likes and dislikes for each video, and what are their corresponding video names?", "id" : "Q6", "header" : ["Video name", "Liked videos"]})
   QuestionsDetails.append({"question" : "7.What is the total number of views for each channel, and what are their corresponding channel names?", "id" : "Q7", "header" : ["Channel name", "Channel views"]})
   QuestionsDetails.append({"question" : "8.What are the names of all the channels that have published videos in the year 2022?", "id" : "Q8", "header" : ["Channel name", "Published videos in the year 2022"]})
   QuestionsDetails.append({"question" : "9.What is the average duration of all videos in each channel, and what are their corresponding channel names?", "id" : "Q9", "header" : ["Channel name", "Avg Duration"]})
   QuestionsDetails.append({"question" : "10.Which videos have the highest number of comments, and what are their corresponding channel names?", "id" : "Q10", "header" : ["Channel name", "Video name", "Comments count"]})
   
   questions = []
   for item in QuestionsDetails:
        questions.append(item["question"])

   id = ""
   header = []
   question = st.selectbox('Select any question to get Insights : ', questions)
   for qItem in QuestionsDetails:
     if(qItem["question"] == question):
        id = qItem["id"]
        header = qItem["header"]
        break

   submitShowAnswer = st.button("Show Answer")
   if submitShowAnswer:
    df = pd.DataFrame(mf.getQA(id, ""), columns=(header))
    df.index = np.arange(1, len(df) + 1)
    st.dataframe(df)









