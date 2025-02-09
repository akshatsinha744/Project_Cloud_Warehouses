Data Warehouse for Sparkify

Project Overview

This project builds an ETL pipeline for a music streaming startup, Sparkify, using Amazon Redshift. The pipeline extracts song and log data from S3, stages them in Redshift, and transforms them into a set of dimensional tables optimized for analytical queries.

Schema Design

The schema follows a star schema with the following tables:

Fact Table

songplays: Stores records of song play events.

Dimension Tables

users: Stores user information.

songs: Stores song details.

artists: Stores artist details.

time: Stores timestamp details.

Files

create_tables.py: Creates tables in Redshift.

etl.py: Loads and processes data into Redshift.

sql_queries.py: Contains SQL queries for table creation and data insertion.

dwh.cfg: Configuration file with Redshift credentials.

Running the Pipeline

Create a Redshift cluster and configure dwh.cfg.

Run python create_tables.py to set up the database schema.

Run python etl.py to load and transform data.

Use Redshift's Query Editor to validate data.

