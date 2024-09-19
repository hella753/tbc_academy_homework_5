import sqlite3
from typing import Optional, List, Tuple
from data_generator import DataGenerator


class Database:
    """
    Database class to handle SQLite3 database operations.
    """

    def __init__(self, db_name: str):
        """
        Constructor for the Database.

        :param db_name: Name of the DB(without ext.) that will be created.

        Initializes books and authors variables to store data;
        db_name which will be the name of the DB and adds the '.sqlite3'
        extension; connection to the SQLite3 database and cursor for
        executing queries.
        """
        self._books: Tuple = tuple((),)
        self._authors: Tuple = tuple((),)
        self.db_name = f"{db_name}.sqlite3"
        self._conn = sqlite3.connect(self.db_name)
        self._cursor = self._conn.cursor()

    def create_table(self, table_name: str, fields: str) -> None:
        """
        Create a table in the database if it doesn't exist.

        :param table_name: Name of the table to create.
        :param fields: str that defines the fields and types in SQL format.
        """
        query = f"""CREATE TABLE IF NOT EXISTS {table_name} ({fields})"""""
        self._cursor.execute(query)
        self._conn.commit()

    def generate_fake_data(
        self,
        books_range: int,
        authors_range: int
    ) -> List[Tuple]:
        """
        Generate fake data for Books & Authors using the DataGenerator class.

        :param books_range: The number of books to generate.
        :param authors_range: The number of authors to generate.

        Calls the DataGenerator class and creates random authors and books.
        Stores the data in the 'books' and 'authors' variables.

        :return: List of tuples containing books and authors.
        """
        data_gen = DataGenerator()
        self._books = tuple(
            data_gen.generate_books(
                books_range,
                authors_range
            )
        )
        self._authors = tuple(
            data_gen.generate_authors(
                authors_range
            )
        )
        return [self._books, self._authors]

    def insert_data(self, table_name: str, columns: str, data: Tuple) -> None:
        """
        Insert data into the table.

        :param table_name: Name of the table to insert data into.
        :param columns: String representing the column names in the table
        :param data: List of tuples containing the data to insert.

        Generates the number of placeholders and inserts the data.
        """
        col_num = len(columns.split(", "))
        quest_marks = ', '.join(['?'] * col_num)
        self._cursor.executemany(
            f"""INSERT INTO {table_name} ({columns}) VALUES ({quest_marks})""",
            data
        )
        self._conn.commit()

    def fetch_data(
        self,
        table_name: str,
        selected: Optional[str] = '*',
        condition: Optional[str] = '',
        limit: Optional[str] = ''
    ) -> List[Tuple]:
        """
        Fetch data from the table.

        :param table_name: Name of the table to fetch data from.
        :param selected: The columns to retrieve (default is "*")
        :param condition: Optional SQL condition
        :param limit: The number of rows to fetch, also optional
        :return: List of tuples containing the query result.
        """
        query = f"""SELECT {selected} FROM {table_name} {condition} {limit}"""
        self._cursor.execute(query)
        self._conn.commit()
        return self._cursor.fetchall()

    def close(self) -> None:
        """
        Close the connection.

        Should be called when all database operations are done
        """
        self._conn.close()
