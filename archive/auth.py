from database import conn, cursor

def register(username,password):

    try:
        cursor.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (username,password)
        )

        conn.commit()
        return True

    except:
        return False


def login(username,password):

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username,password)
    )

    return cursor.fetchone()