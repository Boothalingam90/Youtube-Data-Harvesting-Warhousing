# Youtube Data Harvesting & Warhousing

### Project Overview

The YouTube Data Management Tool is a comprehensive solution tailored for efficient handling of YouTube channel data. It integrates seamlessly with Google API to retrieve detailed insights such as channel statistics, video metrics, and audience engagement. Through intuitive functionalities and a user-friendly interface, users can effortlessly search, harvest, warehouse, and analyze data from YouTube channels.

### Basic Workflow

1. **Search**: Empowers users to query and explore YouTube data based on channel name, video title, or description. This feature facilitates targeted data retrieval for further analysis.

2. **Harvesting**: With the ability to input a YouTube channel ID, the tool fetches a wealth of information including channel name, subscriber count, total video count, playlist ID, video ID, likes, dislikes, and comments for each video. This data collection process is streamlined through Google API integration.

3. **Warehousing**: The tool provides an option to store collected data in a MongoDB database, serving as a robust data lake. Users can effortlessly manage and organize data from multiple YouTube channels within this centralized repository. Additionally, selected data can be migrated from the data lake to a SQL database for structured analysis and reporting.

4. **Questions**: Users can gain actionable insights by leveraging predefined questions tailored to extract valuable information from YouTube channel data. These insights aid in understanding channel performance, audience behavior, and content engagement.

### Execution

#### Tabs:

1. **Search**: Enables users to perform targeted searches based on specific criteria such as channel name, video title, or description. This feature enhances data exploration and facilitates informed decision-making.

2. **Harvesting**: Facilitates seamless data retrieval by allowing users to input a YouTube channel ID and fetch comprehensive data with the click of a button. The integration with Google API ensures accurate and up-to-date information retrieval.

3. **Warehousing**: Offers robust data management capabilities, allowing users to store, organize, and migrate YouTube channel data between MongoDB and SQL databases. This feature streamlines data storage and enhances accessibility for further analysis.

4. **Questions**: Provides a framework for generating actionable insights from YouTube channel data. Users can select from a range of predefined questions to analyze channel performance, audience engagement, and content effectiveness.

### Dependencies

- Google API
- MongoDB
- SQL database (e.g., MySQL, PostgreSQL)

### Usage Guide

1. Clone the repository to your local machine.
2. Install the necessary dependencies as specified in the requirements file.
3. Configure Google API credentials for seamless integration.
4. Ensure MongoDB and SQL databases are installed and running.
5. Launch the application and navigate through the intuitive tabs to perform desired actions such as search, harvesting, warehousing, and analysis.

# startup file : streamlit run streamlit_app.py
