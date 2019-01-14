import MySQLdb
from {PROJECT_NAME} import app


# DB CLASS
class ConnectDB:
    def __init__(self):
        self.db = MySQLdb.connect(host=app.config.get("{PROJECT_NAME}_DB_HOST"),  # your host
                             user=app.config.get("{PROJECT_NAME}_DB_USER"),       # username
                             passwd=app.config.get("{PROJECT_NAME}_DB_PASSWORD"),     # password
                             db=app.config.get("{PROJECT_NAME}_DB_NAME"),   # name of the database
                             port=app.config.get("{PROJECT_NAME}_DB_PORT"),
                             use_unicode=True,
                             charset="utf8mb4"
        )
        self.db.commit()


# Operation Class
class AnyQuery:
    def __init__(self):
        # Create Cursor for Account
        self.db = ConnectDB().db
        self.cursor = self.db.cursor()
        self.results = None

    # Limiting Memory Usage by Chunking the data
    def resultIter(self, cursor, arraysize=1000):
        """An iterator that uses fetchmany to keep memory usage down"""
        while True:
            results = cursor.fetchmany(arraysize)
            if not results:
                break
            for result in results:
                yield result

    def execute(self, query, parameters=None):
        method = "SELECT"
        if query.split()[0].lower() == "insert":
            method = "INSERT"
        if query.split()[0].lower() == "select":
            method = "SELECT"
        if query.split()[0].lower() == "update":
            method = "UPDATE"
        if query.split()[0].lower() == "delete":
            method = "DELETE"

        if method == "INSERT":
            if parameters:
                self.cursor.execute(query, parameters)
            else:
                self.cursor.execute(query)

            self.results = True

        if method == "SELECT":
            if parameters:
                self.cursor.execute(query, parameters)
            else:
                self.cursor.execute(query)
            self.results = []
            for i in self.resultIter(self.cursor):
                self.results.append(i)
            self.results = tuple(self.results)

        if method == "UPDATE":
            if parameters:
                self.cursor.execute(query, parameters)
            else:
                self.cursor.execute(query)
            self.results = True

        if method == "DELETE":
            if parameters:
                self.cursor.execute(query, parameters)
            else:
                self.cursor.execute(query)
            self.results = True

        # Transaction Commits and close connection.
        self.db.commit()
        self.cursor.close()
        self.db.close()

        # Return Data
        return self.results
