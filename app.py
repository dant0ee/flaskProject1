from datetime import date
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, render_template


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workout-database-file.db'
db = SQLAlchemy(app)

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(50))
    duration = db.Column(db.Integer)
    calories_burned = db.Column(db.Integer)
    date = db.Column(db.Date)

    def __repr__(self):
        return f"Exercise(name='{self.name}', type='{self.type}', duration={self.duration}, calories_burned={self.calories_burned}, date='{self.date}')"

# Routes
@app.route('/')
def index():
    today = date.today()
    exercises = Exercise.query.filter(Exercise.date == today).all()
    total_calories = sum(exercise.calories_burned for exercise in exercises)

    return render_template('index.html', exercises=exercises, total_calories=total_calories)

@app.route('/exercise/<int:exercise_id>')
def exercise_detail(exercise_id):
    exercise = Exercise.query.get_or_404(exercise_id)
    return render_template('exercise_detail.html', exercise=exercise)


with app.app_context():
    db.create_all()
    app.run()
