import sqlite3


connection = sqlite3.connect('data.db')
sql = connection.cursor()


sql.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER,
            phone_number TEXT,
            username TEXT
    )
    """
)


# def, INSERT INTO, connection.commit()
def add_user(telegram_id, phone_number, username):
    connection = sqlite3.connect('data.db')
    sql = connection.cursor()

    sql.execute(
        """
            INSERT INTO users (telegram_id, phone_number, username) VALUES (?,?,?)

        """, (telegram_id, phone_number, username)
    )

    connection.commit()
    connection.close()


def delete_user(telegram_id):
    connection = sqlite3.connect('data.db')
    sql = connection.cursor()

    sql.execute(
        """

        DELETE FROM users WHERE telegram_id=?;

        """, (telegram_id,)
    )

    connection.commit()
    connection.close()


def check_user(telegram_id):
    connection = sqlite3.connect('data.db')
    sql = connection.cursor()

    user = sql.execute(
        """
            SELECT telegram_id FROM users WHERE telegram_id=?;
        """, (telegram_id,)

    ).fetchone()

    if user:
        return True
    
    else:
        return False

