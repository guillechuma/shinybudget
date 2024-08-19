import sqlite3

class Database:
    def __init__(self, db_name):
        """
        Initializes a new Database instance.

        Args:
            db_name (str): The name of the SQLite database file to connect to.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=None):
        """
        Executes a SQL query with optional parameters and commits the changes to the database.
        
        Args:
            query (str): The SQL query to execute.
            params (Optional[Tuple]): The parameters to substitute into the query.
        
        Returns:
            None
        """
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.conn.commit()

    def fetch_all(self, query, params=None):
        """
        Executes a SQL query and returns all rows that match the query as a list of tuples.
        
        Args:
            query (str): The SQL query to execute.
            params (Optional[Tuple]): The parameters to substitute into the query.
            
        Returns:
            List[Tuple]: A list of tuples representing the rows that match the query.
        """
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def close(self):
        """
        Closes the database connection.

        This method should be called when the database operations are completed to free up resources.
        """
        self.conn.close()