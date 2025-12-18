import psycopg2

db_info = {
    "host": "localhost",
    "port": 5433,
    "dbname": "testdb",
    "user": "postgres",
    "password": "postgres"
}

with psycopg2.connect(**db_info) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users;")
        rows = cur.fetchall()
        for row in rows:
            print(row)