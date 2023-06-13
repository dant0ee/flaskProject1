from app import db

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(50))
    duration = db.Column(db.Integer)
    calories_burned = db.Column(db.Integer)
    date = db.Column(db.Date)

    def __repr__(self):
        return f"Exercise(name='{self.name}', type='{self.type}', duration={self.duration}, calories_burned={self.calories_burned}, date='{self.date}')"
