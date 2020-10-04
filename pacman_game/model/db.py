from pkg_resources import resource_filename
import sqlite3

# Singleton class

class DB():
    def __init__(self):
        path = resource_filename("pacman_game", "data/db.sqlite")
        self._connection = sqlite3.connect(path)

    def cursor(self):
        return self._connection.cursor()

    def commit(self):
        self._connection.commit()

    def close(self):
        self._connection.close()


