--CREATE DATABASE Youtube
--GO
USE Youtube
GO

--SELECT * FROM dbo.Channel (NOLOCK) -- WHERE channel_id = 'UCs5rmLvEzb-AVKSXM3oO8Zg' 
--SELECT * FROM dbo.Playlist (NOLOCK) --WHERE playlist_id = 'UUs5rmLvEzb-AVKSXM3oO8Zg' 
--SELECT * FROM dbo.Videos(NOLOCK) --WHERE Playlist_id = 'UUs5rmLvEzb-AVKSXM3oO8Zg' 
--SELECT * FROM dbo.Comment (NOLOCK) --WHERE video_id in (SELECT video_id FROM dbo.Videos(NOLOCK) WHERE Playlist_id = 'UUs5rmLvEzb-AVKSXM3oO8Zg' )


--DELETE dbo.Comment WHERE video_id in (SELECT video_id FROM dbo.Videos(NOLOCK) WHERE Playlist_id = 'UUs5rmLvEzb-AVKSXM3oO8Zg' )
--DELETE dbo.Videos WHERE playlist_id = 'UUs5rmLvEzb-AVKSXM3oO8Zg' 
--DELETE dbo.Playlist WHERE playlist_id = 'UUs5rmLvEzb-AVKSXM3oO8Zg' 
--DELETE dbo.Channel WHERE channel_id = 'UCs5rmLvEzb-AVKSXM3oO8Zg' 

--UCJcCB-QYPIBcbKcBQOTwhiA
--UCnC8SAZzQiBGYVSKZ_S3y4Q
--UCBHyHIpO3MzU8fiNM3FbFcA
--UCYuQwKOCk8hipEa6uRhyHGQ
--UCJhWD-Sy_VDbzxFvFJJE_Hw
--UCs5rmLvEzb-AVKSXM3oO8Zg

--UCgf2bJZYZ6JG9ObTfKwAS_A
--UCsVLwAo9-qB3MIU18J7nJSg
--UCB53hX_kvPKTYxbxiUhBHXA
--UC38tpGV1AydcEOMomOgNwNA
--UCOUuAcAMArRoy6k6zJ3uAxQ
--UCOJfVamQGGG-eSrf1AqzMOQ
--UCQjt8LFjuRt6sRLWFWLGMyw - comedy tv

--DELETE dbo.Channel
--DELETE dbo.Playlist
--DELETE dbo.Videos
--DELETE dbo.Comment


--ALTER table Channel 
--Alter column Channel_views BIGINT

--1.What are the names of all the videos and their corresponding channels?

--SELECT v.video_name, c.channel_name
--FROM dbo.videos v 
--	JOIN dbo.Playlist p ON p.playlist_id = v.playlist_id
--	JOIN dbo.Channel c ON c.channel_id = p.channel_id

--2.Which channels have the most number of videos, and how many videos do they have?

--SELECT c.channel_name, COUNT(v.playlist_id) as [No_of_Videos]
--FROM dbo.videos v 
--	JOIN dbo.Playlist p ON p.playlist_id = v.playlist_id
--	JOIN dbo.Channel c ON c.channel_id = p.channel_id
--GROUP BY v.playlist_id, c.channel_name
--ORDER BY COUNT(v.playlist_id) DESC

--3.What are the top 10 most viewed videos and their respective channels?

--SELECT TOP 10 MAX(v.view_count) as [Most_viewed_videos], v.video_name, c.channel_name
--FROM dbo.videos v 
--	JOIN dbo.Playlist p ON p.playlist_id = v.playlist_id
--	JOIN dbo.Channel c ON c.channel_id = p.channel_id
--GROUP BY v.video_name, c.channel_name
--ORDER BY MAX(v.view_count) DESC

--4.How many comments were made on each video, and what are their corresponding video names?

--SELECT v.video_name, v.comment_count FROM dbo.videos v  ORDER BY v.comment_count DESC

--5.Which videos have the highest number of likes, and what are their corresponding channel names?

--SELECT MAX(v.like_count) as [Most_liked_videos], v.video_name, c.channel_name 
--FROM dbo.videos v  
--	JOIN dbo.Playlist p ON p.playlist_id = v.playlist_id
--	JOIN dbo.Channel c ON c.channel_id = p.channel_id
--GROUP BY v.video_name, c.channel_name
--ORDER BY MAX(v.like_count) DESC

--6.What is the total number of likes and dislikes for each video, and what are their corresponding video names?

--SELECT v.video_name, v.like_count AS Likes_Count
--FROM dbo.videos v  
--ORDER BY v.like_count DESC

--7.What is the total number of views for each channel, and what are their corresponding channel names?

--SELECT c.channel_name, c.channel_views FROM dbo.Channel c  ORDER BY c.channel_views DESC

--8.What are the names of all the channels that have published videos in the year 2022?

--SELECT c.channel_name, YEAR(v.published_date) AS [Year]
--FROM dbo.videos v  
--	JOIN dbo.Playlist p ON p.playlist_id = v.playlist_id
--	JOIN dbo.Channel c ON c.channel_id = p.channel_id
--GROUP BY c.channel_name, YEAR(v.published_date )
--HAVING YEAR(v.published_date ) = 2022

--9.What is the average duration of all videos in each channel, and what are their corresponding channel names?

--10.Which videos have the highest number of comments, and what are their corresponding channel names?

--SELECT MAX(v.comment_count) as [Most_commented_videos], v.video_name, c.channel_name 
--FROM dbo.videos v  
--	JOIN dbo.Playlist p ON p.playlist_id = v.playlist_id
--	JOIN dbo.Channel c ON c.channel_id = p.channel_id
--GROUP BY v.video_name, c.channel_name
--ORDER BY MAX(v.comment_count) DESC

SELECT * FROM dbo.Channel c 
SELECT * FROM dbo.Playlist p 
SELECT * FROM dbo.Videos v 
SELECT * FROM dbo.Comment cc 

DECLARE @channel_id VARCHAR(255) = NULL --'UCJcCB-QYPIBcbKcBQOTwhiA'
DECLARE	@channel_name VARCHAR(255) = NULL -- 'Nikhil Mathew'
DECLARE	@video_name VARCHAR(255) = NULL --'Nikhil Mathew'
DECLARE	@video_description NVARCHAR(MAX) = NULL --'Nikhil Mathew'

--SELECT v.* FROM dbo.Videos v
-- JOIN dbo.Playlist p ON p.playlist_id = v.playlist_id
-- JOIN dbo.Channel c on c.channel_id = p.channel_id
--WHERE (@channel_id IS NULL OR c.channel_id = @channel_id)
--	AND (@channel_name IS NULL OR c.channel_name = @channel_name)
--	AND (@video_name IS NULL OR v.video_name like '%' + @video_name + '%' )
--	AND (@video_description IS NULL OR v.video_description like '%' + @video_description + '%' )

--SELECT * FROM Videos

--SELECT SUM(reply_count) FROm comment WHERE reply_count > 0
GO


--DECLARE @channel_id VARCHAR(255), @playlist_id VARCHAR(255)
--SELECT @playlist_id = playlist_id FROM dbo.Playlist WHERE channel_id = @channel_id;
--DELETE dbo.Comment WHERE video_id in (SELECT video_id FROM dbo.Videos(NOLOCK) WHERE Playlist_id = @playlist_id);
--DELETE dbo.Videos WHERE playlist_id = @playlist_id; 
--DELETE dbo.Playlist WHERE playlist_id = @playlist_id;
--DELETE dbo.Channel WHERE channel_id = @channel_id;


--SELECT c.channel_name, CAST(DATEADD(ms, AVG(DATEDIFF(ms,'00:00:00',v.durationtime)),'00:00:00' ) AS TIME) AS avg_duration
--FROM dbo.videos v
--	JOIN dbo.Playlist p ON p.playlist_id = v.playlist_id
--	JOIN dbo.Channel c on c.channel_id = p.channel_id
--GROUP BY c.channel_name
--ORDER BY avg_duration DESC;

--SELECT * FROM videos WHERE Duration = 'P0D'

--EXEC dbo.getChannelData @Type = 'CDD', @channel_id = 'UCgf2bJZYZ6JG9ObTfKwAS_A'
--EXEC dbo.getChannelData @Type = 'CDA', @channel_id = 'UCgf2bJZYZ6JG9ObTfKwAS_A'
--EXEC dbo.getChannelData @Type = 'LD', @channel_id = '', @channel_name = 'Late Night Gaming', @video_name = '1st Time Playing Fortnite', @video_description = ''
--EXEC dbo.getChannelData @Type = 'Q9'

--UCgf2bJZYZ6JG9ObTfKwAS_A
--UCsVLwAo9-qB3MIU18J7nJSg
--UCB53hX_kvPKTYxbxiUhBHXA
--UC38tpGV1AydcEOMomOgNwNA
--UCOUuAcAMArRoy6k6zJ3uAxQ
--UCOJfVamQGGG-eSrf1AqzMOQ
--UCQjt8LFjuRt6sRLWFWLGMyw
--UCIaNGpCwJflexzNnmYALIWg
--UCvY6htBP3UocMx6OXFvjx5g
--UCS2d0K7_KTDZfsbNIgeiHzQ
--UCE54nGKgMDCRH_932ugw3iw
--UCmIhhF-GDGqhdvsMMncheZg
--UCNhbEmLz8kQtRJ_Jv5-ob6A