from app.database.sqldb import SQLDatabase


class SQLSession:

    def __init__(self):
        self.db = SQLDatabase()

    def insert(self, table, columns, values_types, values):
        sql_columns = "%s" % (columns,)
        sql_values_type = "VALUES %s" % (values_types,)
        sql = f"INSERT INTO {table} {sql_columns} {sql_values_type}".replace("'", "")

        cursor = self.db.get_database().cursor()
        cursor.execute(sql, values)
        self.db.get_database().commit()
        cursor.close()
        del self.db

    def find(self, table, columns=None):
        if columns:
            sql_columns = " %s" % (columns,)
        else:
            sql_columns = "*"
        sql = f"SELECT  {sql_columns} FROM {table}".replace("'", "")

        cursor = self.db.get_database().cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        del self.db
        return result

    def find_where(self, table, column, search_value):
        sql = f"SELECT * FROM {table} WHERE {column} = '{search_value}'"
        cursor = self.db.get_database().cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        del self.db
        return result
