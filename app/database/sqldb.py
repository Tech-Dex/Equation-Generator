import sys

import mariadb

from app.config import DATABASE, DB_USER, DB_USER_PASSWORD, HOST, PORT, TABLE


class Database:
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


db = Database()


def get_database():
    return db.client


def create_table():
    _db = get_database()
    if not is_table_created(_db):
        cursor = _db.cursor()
        sql = f"CREATE TABLE {TABLE} (id INT AUTO_INCREMENT PRIMARY KEY, equation VARCHAR(255), result VARCHAR(255), winner VARCHAR(255))"
        cursor.execute(sql)


def is_table_created(_db):
    cursor = _db.cursor()
    cursor.execute("SHOW TABLES")
    for name, in cursor:
        if name == TABLE:
            return True
    return False


class SQLSession:

    def __init__(self):
        self.db = get_database()

    def insert(self, table, columns, values_types, values):
        sql_columns = "%s" % (columns,)
        sql_values_type = "VALUES %s" % (values_types,)
        sql = f"INSERT INTO {table} {sql_columns} {sql_values_type}".replace("'", "")

        cursor = self.db.cursor()
        cursor.execute(sql, values)
        self.db.commit()

    def select(self, table, columns=None):
        if columns:
            sql_columns = " %s" % (columns,)
        else:
            sql_columns = "*"
        sql = f"SELECT  {sql_columns} FROM {table}".replace("'", "")

        cursor = self.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
