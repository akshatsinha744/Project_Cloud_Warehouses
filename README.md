# Cloud Data Warehousing with AWS Redshift

## Project Overview
This project builds a **Cloud Data Warehouse** on AWS using **Redshift** to store and analyze song play data for **Sparkify**, a fictional music streaming company. The data comes from JSON log files and song metadata stored in S3.

## Technologies Used
- **AWS Redshift** for cloud data warehousing
- **AWS S3** for data storage
- **Python (ETL processing)**
- **PostgreSQL (SQL for Redshift)**

## Database Schema (Star Schema)
### **Fact Table**
- **songplays** - Records in event data associated with song plays (log data).
  - `songplay_id`, `start_time`, `user_id`, `level`, `song_id`, `artist_id`, `session_id`, `location`, `user_agent`

### **Dimension Tables**
- **users** - Users in the app.
  - `user_id`, `first_name`, `last_name`, `gender`, `level`
- **songs** - Songs in the music database.
  - `song_id`, `title`, `artist_id`, `year`, `duration`
- **artists** - Artists in the music database.
  - `artist_id`, `name`, `location`, `latitude`, `longitude`
- **time** - Timestamps of records in songplays, broken down into specific units.
  - `start_time`, `hour`, `day`, `week`, `month`, `year`, `weekday`

## ETL Process
1. **Extract** - Reads JSON data from S3.
2. **Transform** - Parses event log files and extracts required fields.
3. **Load** - Loads the transformed data into **AWS Redshift**.

## Running the Pipeline
1. **Launch AWS Redshift Cluster** and configure security settings.
2. **Run `create_tables.py`** to initialize the database.
3. **Run `etl.py`** to load data into Redshift.
4. **Query data in Redshift** to verify.

## Example Queries
```sql
SELECT user_id, COUNT(*) AS play_count 
FROM songplays 
GROUP BY user_id 
ORDER BY play_count DESC;
```
