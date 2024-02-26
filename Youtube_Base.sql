--CREATE DATABASE Youtube
--GO
USE Youtube
GO

IF (EXISTS (SELECT * 
                 FROM INFORMATION_SCHEMA.TABLES 
                 WHERE TABLE_SCHEMA = 'dbo' 
                 AND  TABLE_NAME = 'Comment'))
BEGIN
    DROP TABLE dbo.Comment
END

IF (EXISTS (SELECT * 
                 FROM INFORMATION_SCHEMA.TABLES 
                 WHERE TABLE_SCHEMA = 'dbo' 
                 AND  TABLE_NAME = 'Videos'))
BEGIN
    DROP TABLE dbo.Videos
END

IF (EXISTS (SELECT * 
                 FROM INFORMATION_SCHEMA.TABLES 
                 WHERE TABLE_SCHEMA = 'dbo' 
                 AND  TABLE_NAME = 'Playlist'))
BEGIN
    DROP TABLE dbo.Playlist
END

IF (EXISTS (SELECT * 
                 FROM INFORMATION_SCHEMA.TABLES 
                 WHERE TABLE_SCHEMA = 'dbo' 
                 AND  TABLE_NAME = 'Channel'))
BEGIN
    DROP TABLE dbo.Channel
END

IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'channel_insert')
DROP PROCEDURE channel_insert
GO

IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'playlist_insert')
DROP PROCEDURE playlist_insert
GO

IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'video_insert')
DROP PROCEDURE video_insert
GO

IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'comment_insert')
DROP PROCEDURE comment_insert
GO

IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'getChannelData')
DROP PROCEDURE getChannelData
GO

CREATE TABLE Channel
(
	channel_id				VARCHAR(255) UNIQUE,
	channel_name			NVARCHAR(255),
	channel_type			VARCHAR(255),
	channel_views			BIGINT,
	channel_description		NVARCHAR(255),
	channel_status			VARCHAR(255),
)
GO

CREATE TABLE Playlist
(
	playlist_id				VARCHAR(255) UNIQUE,
	channel_id				VARCHAR(255) FOREIGN KEY REFERENCES Channel(channel_id),
	playlist_name			NVARCHAR(255)
)
GO

CREATE TABLE Videos
(
	video_id				VARCHAR(255) UNIQUE,
	playlist_id				VARCHAR(255) FOREIGN KEY REFERENCES Playlist(playlist_id),
	video_name				NVARCHAR(255),
	video_description		NVARCHAR(MAX),
	published_date			DATETIME,
	view_count				INT,
	like_count				INT,
	dislike_count			INT,
	favorite_count			INT,
	comment_count			INT,
	duration				VARCHAR(255),
	durationtime			TIME,
	thumbnail				NVARCHAR(255),
	caption_status			VARCHAR(255),
)
GO

CREATE TABLE Comment
(
	comment_id					VARCHAR(255) UNIQUE,
	video_id					VARCHAR(255) FOREIGN KEY REFERENCES Videos(video_id),
	comment_text				NVARCHAR(MAX),
	comment_author				NVARCHAR(255),
	comment_published_date		DATETIME,
	like_count					INT,
	reply_count					INT,
	comment_key					VARCHAR(255),
)
GO

CREATE PROC channel_insert
(
		@channel_id				VARCHAR(255),
		@channel_name			NVARCHAR(255),
		@channel_type			VARCHAR(255),
		@channel_views			BIGINT,
		@channel_description	NVARCHAR(255),
		@channel_status			VARCHAR(255)
)
AS BEGIN
	INSERT INTO dbo.Channel 
	(	
		channel_id, 
		channel_name, 
		channel_type, 
		channel_views,
		channel_description,
		channel_status
	) 
	VALUES
	(	
		@channel_id, 
		@channel_name, 
		@channel_type, 
		@channel_views,
		@channel_description,
		@channel_status
	) 

END
GO

CREATE PROC playlist_insert
(
	@playlist_id			VARCHAR(255),
	@channel_id				VARCHAR(255),
	@playlist_name			NVARCHAR(255)
)
AS BEGIN
	INSERT INTO dbo.Playlist 
	(	
		playlist_id,
		channel_id,
		playlist_name
	) 
	VALUES
	(	
		@playlist_id,
		@channel_id,
		@playlist_name
	) 

END
GO

CREATE PROC video_insert
(
	@video_id				VARCHAR(255),
	@playlist_id			VARCHAR(255),
	@video_name				NVARCHAR(255),
	@video_description		NVARCHAR(MAX),
	@published_date			DATETIME,
	@view_count				INT,
	@like_count				INT,
	@dislike_count			INT,
	@favorite_count			INT,
	@comment_count			INT,
	@duration				VARCHAR(255),
	@thumbnail				NVARCHAR(255),
	@caption_status			VARCHAR(255),
	@durationtime			TIME
)
AS BEGIN
	INSERT INTO dbo.Videos 
	(	
		video_id,
		playlist_id,
		video_name,
		video_description,
		published_date,		
		view_count,			
		like_count,			
		dislike_count,	
		favorite_count,		
		comment_count,		
		duration,
		thumbnail,
		caption_status,
		durationtime
	) 
	VALUES
	(	
		@video_id,
		@playlist_id,
		@video_name,
		@video_description,
		@published_date,		
		@view_count,			
		@like_count,			
		@dislike_count,	
		@favorite_count,		
		@comment_count,		
		@duration,
		@thumbnail,
		@caption_status,
		@durationtime
	) 
END
GO

CREATE PROC comment_insert
(
	@comment_id					VARCHAR(255),
	@video_id					VARCHAR(255),
	@comment_text				NVARCHAR(MAX),
	@comment_author				NVARCHAR(255),
	@comment_published_date		DATETIME,
	@like_count					INT,
	@reply_count				INT,
	@comment_key				VARCHAR(255)
)
AS BEGIN
	INSERT INTO dbo.Comment 
	(	
		comment_id,				
		video_id,				
		comment_text,			
		comment_author,			
		comment_published_date,
		like_count,
		reply_count,
		comment_key
	) 
	VALUES
	(	
		@comment_id,				
		@video_id,				
		@comment_text,			
		@comment_author,			
		@comment_published_date,
		@like_count,
		@reply_count,
		@comment_key
	) 
END
GO

CREATE PROC dbo.getChannelData
(
	@Type				VARCHAR(3) = '',
	@channel_id			VARCHAR(255) = NULL,
	@channel_name		VARCHAR(255) = NULL,
	@video_name			VARCHAR(255) = NULL,
	@video_description	NVARCHAR(MAX) = NULL
)
AS BEGIN 
	
	IF @Type = 'LD'
	BEGIN
		--List of Videos based on condition

		SELECT  v.video_name, v.video_description, v.published_date, view_count, like_count, c.channel_name 
		FROM dbo.Videos v
		 JOIN dbo.Playlist p ON p.playlist_id = v.playlist_id
		 JOIN dbo.Channel c on c.channel_id = p.channel_id
		WHERE (@channel_id IS NULL OR @channel_id = '' OR c.channel_id = @channel_id)
			AND (@channel_name IS NULL OR @channel_name = '' OR c.channel_name like '%' + @channel_name  + '%')
			AND (@video_name IS NULL OR @video_name = '' OR v.video_name like '%' + @video_name + '%' )
			AND (@video_description IS NULL OR @video_description = '' OR v.video_description like '%' + @video_description + '%' )

	END
	ELSE IF @Type = 'CDA'
	BEGIN
		--List of Channels

		SELECT channel_id, channel_name, channel_type, channel_views, channel_description, channel_status FROM dbo.Channel c

	END
	ELSE IF @Type = 'CDD'
	BEGIN
		--Channels details by Id

		SELECT channel_id, channel_name, channel_type, channel_views, channel_description, channel_status FROM dbo.Channel c WHERE channel_id = @channel_id

	END
	ELSE IF @Type = 'Q1'
	BEGIN

		--1.What are the names of all the videos and their corresponding channels?

		SELECT c.channel_name, v.video_name
		FROM dbo.videos v 
			JOIN dbo.Playlist p ON p.playlist_id = v.playlist_id
			JOIN dbo.Channel c ON c.channel_id = p.channel_id

	END
	ELSE IF @Type = 'Q2'
	BEGIN

		--2.Which channels have the most number of videos, and how many videos do they have?

		SELECT c.channel_name, COUNT(v.playlist_id) as [No_of_Videos]
		FROM dbo.videos v 
			JOIN dbo.Playlist p ON p.playlist_id = v.playlist_id
			JOIN dbo.Channel c ON c.channel_id = p.channel_id
		GROUP BY v.playlist_id, c.channel_name
		ORDER BY COUNT(v.playlist_id) DESC

	END
	ELSE IF @Type = 'Q3'
	BEGIN

		--3.What are the top 10 most viewed videos and their respective channels?

		SELECT TOP 10  c.channel_name, v.video_name, MAX(v.view_count) as [Most_viewed_videos]
		FROM dbo.videos v 
			JOIN dbo.Playlist p ON p.playlist_id = v.playlist_id
			JOIN dbo.Channel c ON c.channel_id = p.channel_id
		GROUP BY v.video_name, c.channel_name
		ORDER BY MAX(v.view_count) DESC

	END
	ELSE IF @Type = 'Q4'
	BEGIN

		--4.How many comments were made on each video, and what are their corresponding video names?

		SELECT v.video_name, v.comment_count FROM dbo.videos v  ORDER BY v.comment_count DESC

	END
	ELSE IF @Type = 'Q5'
	BEGIN

		--5.Which videos have the highest number of likes, and what are their corresponding channel names?

		SELECT  c.channel_name, v.video_name, MAX(v.like_count) as [Most_liked_videos]
		FROM dbo.videos v  
			JOIN dbo.Playlist p ON p.playlist_id = v.playlist_id
			JOIN dbo.Channel c ON c.channel_id = p.channel_id
		GROUP BY v.video_name, c.channel_name
		ORDER BY MAX(v.like_count) DESC

	END
	ELSE IF @Type = 'Q6'
	BEGIN	

		--6.What is the total number of likes and dislikes for each video, and what are their corresponding video names?

		SELECT v.video_name, v.like_count AS Likes_Count
		FROM dbo.videos v  
		ORDER BY v.like_count DESC

	END
	ELSE IF @Type = 'Q7'
	BEGIN

		--7.What is the total number of views for each channel, and what are their corresponding channel names?

		SELECT c.channel_name, c.channel_views FROM dbo.Channel c  ORDER BY c.channel_views DESC

	END
	ELSE IF @Type = 'Q8'
	BEGIN

		--8.What are the names of all the channels that have published videos in the year 2022?

		SELECT c.channel_name, YEAR(v.published_date) AS [Year]
		FROM dbo.videos v  
			JOIN dbo.Playlist p ON p.playlist_id = v.playlist_id
			JOIN dbo.Channel c ON c.channel_id = p.channel_id
		GROUP BY c.channel_name, YEAR(v.published_date )
		HAVING YEAR(v.published_date ) = 2022

	END
	ELSE IF @Type = 'Q9'
	BEGIN

		--9.What is the average duration of all videos in each channel, and what are their corresponding channel names?

		SELECT c.channel_name, CONVERT(VARCHAR(8), CAST(DATEADD(ms, AVG(DATEDIFF(ms,'00:00:00', v.durationtime)), '00:00:00') AS TIME)) AS avg_duration
		FROM dbo.videos v
			JOIN dbo.Playlist p ON p.playlist_id = v.playlist_id
			JOIN dbo.Channel c on c.channel_id = p.channel_id
		GROUP BY c.channel_name
		ORDER BY avg_duration DESC;

	END
	ELSE IF @Type = 'Q10'
	BEGIN

		--10.Which videos have the highest number of comments, and what are their corresponding channel names?

		SELECT  c.channel_name, v.video_name, MAX(v.comment_count) as [Most_commented_videos]
		FROM dbo.videos v  
			JOIN dbo.Playlist p ON p.playlist_id = v.playlist_id
			JOIN dbo.Channel c ON c.channel_id = p.channel_id
		GROUP BY v.video_name, c.channel_name
		ORDER BY MAX(v.comment_count) DESC

	END
END
GO
