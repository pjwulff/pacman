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
