import psycopg2
from sql_queries import create_table_queries, drop_table_queries

def drop_tables(cur, conn):
    """Drops each table in the Redshift database."""
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

def create_tables(cur, conn):
    """Creates fact and dimension tables in the Redshift database."""
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    """Establishes connection to Redshift and creates tables."""
    conn = psycopg2.connect("host=your-cluster-endpoint dbname=your-db user=your-user password=your-password port=5439")
    cur = conn.cursor()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)
    
    conn.close()

if __name__ == "__main__":
    main()
