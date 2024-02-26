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
	@caption_status			VARCHAR(255)
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
		caption_status
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
		@caption_status
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

