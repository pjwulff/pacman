from ..model.db import DB

class HighScoresController:
    def __init__(self):
        pass

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
