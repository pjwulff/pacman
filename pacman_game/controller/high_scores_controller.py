from ..model.db import DB

## A controller to handle interfacing with the high score table.
class HighScoresController:

    ## Insert a high score into the table, used when the player finishes
    ## a game. The parameters for this function are the initials of the player,
    ## and details of the game that were played.
    #
    # @param initials The initials of the user.
    # @param score The score.
    # @param difficulty The difficulty of the game.
    # @param shape The shape of the maze.
    # @param size The size of the maze.
    @classmethod
    def insert_high_score(cls, initials, score, difficulty, shape, size):
        db = DB()
        cursor = db.cursor()
        cursor.execute(f"""
            INSERT INTO high_scores
            (initials, score, difficulty, shape, size)
            VALUES
            (\"{initials}\", {score}, \"{difficulty}\", \"{shape}\", \"{size}\")""")
        db.commit()
        db.close()

    ## Get a list of high scores, filtered according to some parameters.
    #
    # @param f The parameters by which to filter the results. Should be a
    # dictionary mapping different game characteristics
    # (e.g., "difficulty-easy") to boolean values, indicating if the results
    # should be included or not.
    # @return An ordered, filtered list of high scores. Each list element is
    # a tuple, the first element of which is the initials, the second of which
    # is the score itself.
    @classmethod
    def high_scores(cls, f):
        db = DB()
        cursor = db.cursor()
        filters = []

        if not f["difficulty-easy"]:
            filters += ["(NOT difficulty=\'easy\')"]
        if not f["difficulty-medium"]:
            filters += ["(NOT difficulty=\'medium\')"]
        if not f["difficulty-hard"]:
            filters += ["(NOT difficulty=\'hard\')"]

        if not f["shape-square"]:
            filters += ["(NOT shape=\'square\')"]
        if not f["shape-hexagonal"]:
            filters += ["(NOT shape=\'hexagonal\')"]
        if not f["shape-graph"]:
            filters += ["(NOT shape=\'graph\')"]

        if not f["size-small"]:
            filters += ["(NOT size=\'small\')"]
        if not f["size-medium"]:
            filters += ["(NOT size=\'medium\')"]
        if not f["size-large"]:
            filters += ["(NOT size=\'large\')"]

        f = " AND ".join(filters)
        if f == "":
            cursor.execute("""
            SELECT initials, score
            FROM high_scores
            ORDER BY score DESC;""")
        else:
            cursor.execute(f"""
                SELECT initials, score
                FROM high_scores
                WHERE {f}
                ORDER BY score DESC;""")
        res = cursor.fetchall()
        db.commit()
        db.close()
        return res
