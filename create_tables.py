import psycopg2

commands = [
    """
    CREATE TABLE IF NOT EXISTS movies (
        movie_id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        release_year INT,
        rating REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS genres (
        genre_id SERIAL PRIMARY KEY,
        name VARCHAR(100) UNIQUE NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS actors (
        actor_id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS movie_genres (
        movie_id INT REFERENCES movies(movie_id) ON DELETE CASCADE,
        genre_id INT REFERENCES genres(genre_id) ON DELETE CASCADE,
        PRIMARY KEY (movie_id, genre_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS movie_actors (
        movie_id INT REFERENCES movies(movie_id) ON DELETE CASCADE,
        actor_id INT REFERENCES actors(actor_id) ON DELETE CASCADE,
        PRIMARY KEY (movie_id, actor_id)
    )
    """
]

try:
    connection = psycopg2.connect(
        dbname="moviedb",
        user="lilvariable",
        password="",
        host="localhost",
        port="5432"
    )
    cursor = connection.cursor()

    for command in commands:
        cursor.execute(command)

    connection.commit()
    print("✅ All tables created successfully!")

except Exception as e:
    print("❌ Error:", e)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("🔒 Connection closed.")
