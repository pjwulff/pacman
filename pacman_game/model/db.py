from pkg_resources import resource_filename
import sqlite3

## A class to manange interfacing with the game's database.
class DB():
    ## Create a new database connection.
    def __init__(self):
        path = resource_filename("pacman_game", "data/db.sqlite")
        self._connection = sqlite3.connect(path)

    ## Get a Python-style database cursor for this connection.
    #
    # @return A cursor.
    def cursor(self):
        return self._connection.cursor()

    ## Perform a commit on the changes pending in the database from this
    ## connection.
    def commit(self):
        self._connection.commit()

    ## Close the connection.
    def close(self):
        self._connection.close()


