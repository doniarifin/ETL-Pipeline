import mysql.connector

def load_data(data):

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        ssl_disabled=True
    )

    if db.is_connected():
        print("MySQL connected!")

    cursor = db.cursor()

    # create db
    cursor.execute("CREATE DATABASE IF NOT EXISTS book")

    # reconnect to new db
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="book",
        ssl_disabled=True
    )
    cursor = db.cursor()

    # create tabel
    sql_table = """
        CREATE TABLE IF NOT EXISTS book_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100),
            rating TINYINT,
            price DOUBLE
        )
    """
    cursor.execute(sql_table)

    # insert
    sql_insert = """
        INSERT INTO book_data 
        (title, rating, price)
        VALUES (%s, %s, %s)
    """

    values = [
        (
            row["title"],
            row["rating"],
            row["price"]
        )
        for row in data
    ]

    cursor.executemany(sql_insert, values)
    db.commit()

    print(f"{cursor.rowcount} rows inserted.")

    cursor.execute("SELECT * FROM book_data")
    print(cursor.fetchall())

    db.close()
