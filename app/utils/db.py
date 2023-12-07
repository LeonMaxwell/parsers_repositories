import pymysql
from pymysql.cursors import DictCursor
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


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
        engine = create_engine(f"mysql+pymysql://root:admin@mysql:3306/parsers")
        self.Base = declarative_base(engine)
        metadata = self.Base.metadata
        self.Session = sessionmaker(bind=engine)

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

    def execute_query(self, query):
        with pymysql.connect(**self.config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                results = cursor.fetchall()
                return results

    def add_repositories(self, data):
        from utils.models import Repositories
        session = self.Session
        repositories = Repositories(
            name=data['name'],
            description=str(data['description'])[:100],
            language=data['language'],
            url=data['url']
        )
        session.add(repositories)
        session.commit()
        return True