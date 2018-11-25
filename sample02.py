import sqlite3


def main():
    conn = sqlite3.connect("users.sqlite")
    cursor = conn.cursor()

    sql = "INSERT INTO users (name,age) VALUES ('Bob',90)"

    cursor.execute(sql)

    conn.commit()

    conn.close()


if __name__ == "__main__":
    main()
