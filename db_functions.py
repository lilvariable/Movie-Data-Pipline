import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="moviedb",
        user="lilvariable",   # <-- Replace this
        password="",
        host="localhost",
        port="5432"
    )

# -----------------------------------
# A. INSERT FUNCTIONS
# -----------------------------------

def add_movie(title, release_year=None, rating=None):
    query = """
    INSERT INTO movies (title, release_year, rating)
    VALUES (%s, %s, %s)
    RETURNING movie_id;
    """
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(query, (title, release_year, rating))
        movie_id = cur.fetchone()[0]
        conn.commit()
        return movie_id
    except Exception as e:
        print("❌ Error adding movie:", e)
    finally:
        if conn:
            cur.close()
            conn.close()


def add_genre(name):
    query = """
    INSERT INTO genres (name)
    VALUES (%s)
    ON CONFLICT (name) DO NOTHING
    RETURNING genre_id;
    """
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(query, (name,))
        genre_id = cur.fetchone()
        if genre_id:
            genre_id = genre_id[0]
        conn.commit()
        return genre_id
    except Exception as e:
        print("❌ Error adding genre:", e)
    finally:
        if conn:
            cur.close()
            conn.close()


def add_actor(name):
    query = """
    INSERT INTO actors (name)
    VALUES (%s)
    RETURNING actor_id;
    """
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(query, (name,))
        actor_id = cur.fetchone()[0]
        conn.commit()
        return actor_id
    except Exception as e:
        print("❌ Error adding actor:", e)
    finally:
        if conn:
            cur.close()
            conn.close()


def link_movie_genre(movie_id, genre_id):
    query = """
    INSERT INTO movie_genres (movie_id, genre_id)
    VALUES (%s, %s)
    ON CONFLICT DO NOTHING;
    """
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(query, (movie_id, genre_id))
        conn.commit()
    except Exception as e:
        print("❌ Error linking movie & genre:", e)
    finally:
        if conn:
            cur.close()
            conn.close()


def link_movie_actor(movie_id, actor_id):
    query = """
    INSERT INTO movie_actors (movie_id, actor_id)
    VALUES (%s, %s)
    ON CONFLICT DO NOTHING;
    """
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(query, (movie_id, actor_id))
        conn.commit()
    except Exception as e:
        print("❌ Error linking movie & actor:", e)
    finally:
        if conn:
            cur.close()
            conn.close()

# -----------------------------------
# B. QUERY FUNCTIONS
# -----------------------------------

def get_movie_by_id(movie_id):
    query = """
    SELECT movie_id, title, release_year, rating 
    FROM movies
    WHERE movie_id = %s;
    """
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(query, (movie_id,))
        return cur.fetchone()
    except Exception as e:
        print("❌ Error fetching movie:", e)
    finally:
        if conn:
            cur.close()
            conn.close()


def search_movies(keyword):
    query = """
    SELECT movie_id, title, release_year, rating
    FROM movies
    WHERE title ILIKE %s;
    """
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(query, (f"%{keyword}%",))
        return cur.fetchall()
    except Exception as e:
        print("❌ Error searching movies:", e)
    finally:
        if conn:
            cur.close()
            conn.close()


def list_all_movies():
    query = "SELECT movie_id, title, release_year, rating FROM movies ORDER BY movie_id;"
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(query)
        return cur.fetchall()
    except Exception as e:
        print("❌ Error listing movies:", e)
    finally:
        if conn:
            cur.close()
            conn.close()



