import psycopg2
from sql_queries import copy_table_queries, insert_table_queries

def load_staging_tables(cur, conn):
    """Loads data from S3 into staging tables in Redshift."""
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()

def insert_tables(cur, conn):
    """Inserts data from staging tables into the analytics tables in Redshift."""
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    """Runs the ETL pipeline to load data into Redshift."""
    conn = psycopg2.connect("host=your-cluster-endpoint dbname=your-db user=your-user password=your-password port=5439")
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)
    
    conn.close()

if __name__ == "__main__":
    main()
