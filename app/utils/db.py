import pymysql
from pymysql.cursors import DictCursor


class DatabaseParser:
    def __init__(self):
        self.config = {
            "host": 'mysql',
            "port": 3306,
            'user': 'root',
            'password': 'admin',
            'db': 'parsers',
            'charset': 'utf8mb4',
            'cursorclass': DictCursor
        }
        self.init_bd()

    def init_bd(self):
        name_table = "repositories"
        id_columns = ["id INT AUTO_INCREMENT NOT NULL", "primary key (id)"]
        column_name = "name varchar(255) NOT NULL"
        column_description = "description varchar(255) NULL"
        column_language = "language varchar(255) NULL"
        column_url = "url varchar(255) NULL"
        columns_value = (column_name + ',' + column_description + ',' + column_language + ',' + column_url)

        self.execute_query("CREATE TABLE IF NOT EXISTS %s (%s)"
                                      % (name_table, id_columns[0] + "," + columns_value + "," + id_columns[1]))

    def execute_query(self, query, values=None):
        with pymysql.connect(**self.config) as conn:
            with conn.cursor() as cursor:
                if values:
                    cursor.execute(query, values)
                    cursor.fetchall()
                    conn.commit()
                else:
                    cursor.execute(query)
                    result = cursor.fetchall()
                    return result