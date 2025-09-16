import sqlite3
from typing import List, Dict, Optional, Union

class Database:
    """A helper class to simplify SQLite3 database interactions."""

    def __init__(self, path: str):
        """
        Initialize the Database instance.

        :param path: Path to the SQLite database file.
        """
        self._path = path

    @property
    def path(self) -> str:
        """Get the database file path."""
        return self._path

    @path.setter
    def path(self, value: str):
        """Set the database file path.

        :param value: New path to the SQLite database file.
        :raises ValueError: If the path is not a string.
        """
        if not isinstance(value, str):
            raise ValueError("Path must be a string")
        self._path = value

    def _execute_query(self, query: str, sequence: Optional[Union[tuple, List[tuple]]] = None) -> sqlite3.Cursor:
        """
        Execute a database query.

        :param query: The SQL query to execute.
        :param sequence: Parameters for the query (optional).
        :return: A cursor object.
        :raises sqlite3.Error: If the query execution fails.
        """
        try:
            with sqlite3.connect(self._path) as conn:
                cursor = conn.cursor()
                if sequence:
                    if isinstance(sequence, list) and len(sequence) > 1:
                        cursor.executemany(query, sequence)
                    else:
                        cursor.execute(query, sequence)
                else:
                    cursor.execute(query)
                conn.commit()
                return cursor
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Database error: {e}")

    def db_fetch(self, query: str, sequence: Optional[tuple] = None) -> List[Dict[str, Union[str, int, float]]]:
        """
        Fetch data from the database.

        :param query: The SELECT query to execute.
        :param sequence: Parameters for the query (optional).
        :return: A list of dictionaries representing the fetched rows.
        :raises ValueError: If the query is not a SELECT statement.
        """
        if not query.strip().upper().startswith("SELECT"):
            raise ValueError("Only SELECT queries are allowed")

        cursor = self._execute_query(query, sequence)
        columns = [description[0] for description in cursor.description]
        data_fetched = cursor.fetchall()
        cursor.close()

        return [dict(zip(columns, row)) for row in data_fetched]

    def db_insert(self, query: str, sequence: Optional[Union[tuple, List[tuple]]] = None) -> int:
        """
        Insert data into the database.

        :param query: The INSERT query to execute.
        :param sequence: Parameters for the query (optional).
        :return: The number of rows affected.
        :raises ValueError: If the query is not an INSERT statement.
        """
        if not query.strip().upper().startswith("INSERT"):
            raise ValueError("Only INSERT queries are allowed")

        cursor = self._execute_query(query, sequence)
        return cursor.rowcount

    def db_delete(self, query: str, sequence: Optional[tuple] = None) -> int:
        """
        Delete data from the database.

        :param query: The DELETE query to execute.
        :param sequence: Parameters for the query (optional).
        :return: The number of rows affected.
        :raises ValueError: If the query is not a DELETE statement.
        """
        if not query.strip().upper().startswith("DELETE"):
            raise ValueError("Only DELETE queries are allowed")

        cursor = self._execute_query(query, sequence)
        return cursor.rowcount

    def db_update(self, query: str, sequence: Optional[tuple] = None) -> int:
        """
        Update data in the database.

        :param query: The UPDATE query to execute.
        :param sequence: Parameters for the query (optional).
        :return: The number of rows affected.
        :raises ValueError: If the query is not an UPDATE statement.
        """
        if not query.strip().upper().startswith("UPDATE"):
            raise ValueError("Only UPDATE queries are allowed")

        cursor = self._execute_query(query, sequence)
        return cursor.rowcount