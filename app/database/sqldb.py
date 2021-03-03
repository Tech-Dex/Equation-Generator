import sys

import mariadb

from app.core.config import (
    DATABASE,
    DB_USER,
    DB_USER_PASSWORD,
    HOST,
    PORT)


class SQLDatabase:
    client = None

    def __init__(self):
        try:
            self.client = mariadb.connect(user=DB_USER,
                                          password=DB_USER_PASSWORD,
                                          host=HOST,
                                          port=PORT,
                                          database=DATABASE)
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

    def get_database(self):
        return self.client

    def __del__(self):
        self.client.close()


def create_table(table):
    db = SQLDatabase()
    _db = db.get_database()
    if not is_table_created(_db, table):
        cursor = _db.cursor()
        sql = f"CREATE TABLE {table} (id INT AUTO_INCREMENT PRIMARY KEY, equation VARCHAR(255), result VARCHAR(255), winner VARCHAR(255))"
        cursor.execute(sql)
        cursor.close()
        del db


def is_table_created(_db, table):
    cursor = _db.cursor()
    cursor.execute("SHOW TABLES")
    for name, in cursor:
        if name == table:
            return True
    return False
