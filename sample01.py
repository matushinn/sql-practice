import sqlite3

"""
目標：PythonでSQLを使ってテーブルを作る
"""


def main():
    conn = sqlite3.connect("users.sqlite")
    cursor = conn.cursor()

    #SQLを準備
    sql = """CREATE TABLE users(name TEXT,age INTEGER)"""

    #SQLを実行
    cursor.execute(sql)

    #コミット
    conn.commit()

    #接続をきる
    conn.close()


if __name__ == "__main__":
    main()

