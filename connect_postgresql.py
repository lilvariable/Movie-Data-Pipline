import psycopg2

try:
    # Connect to your PostgreSQL database
    connection = psycopg2.connect(
        dbname="moviedb",
        user="lilvariable",  # same name you use in psql prompt
        password="",               # leave blank if not set
        host="localhost",
        port="5432"
    )

    print("✅ Connected to PostgreSQL successfully!")

    # Create a cursor to interact with the database
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print("PostgreSQL version:", version)

except Exception as e:
    print("❌ Error:", e)

finally:
    if 'connection' in locals() and connection:
        cursor.close()
        connection.close()
        print("🔒 Connection closed.")
