# SQL queries for table creation, copying data from S3, and inserting data

# Drop tables if they exist
drop_table_queries = [
    "DROP TABLE IF EXISTS songplays;", 
    "DROP TABLE IF EXISTS users;", 
    "DROP TABLE IF EXISTS songs;", 
    "DROP TABLE IF EXISTS artists;", 
    "DROP TABLE IF EXISTS time;"
]

# Create tables
create_table_queries = [
    """
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id INT IDENTITY(0,1) PRIMARY KEY,
        start_time TIMESTAMP NOT NULL,
        user_id INT NOT NULL,
        level VARCHAR,
        song_id VARCHAR,
        artist_id VARCHAR,
        session_id INT,
        location VARCHAR,
        user_agent TEXT
    );
    """
]

# Copy data from S3 to staging tables
copy_table_queries = [
    "COPY songplays FROM 's3://your-bucket/songplays' IAM_ROLE 'your-iam-role' FORMAT AS JSON 'auto';"
]

# Insert data into final tables
insert_table_queries = [
    "INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) SELECT start_time, user_id, level, song_id, artist_id, session_id, location, user_agent FROM staging_events;"
]
