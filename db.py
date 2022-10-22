from flask_sqlalchemy import SQLAlchemy 
from flask import Flask
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
Session = sessionmaker(bind=engine)

# mysql://username:password@host:port/database_name
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://admin:dbuserdbuser@e6156.clg4hkuxiisg.us-east-2.rds.amazonaws.com:3306/quiz_data"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Quiz(db.Model):
  __tablename__ = "quiz"
  quiz_id = db.Column(db.Integer, primary_key=True)
  difficulty = db.Column(db.Integer)

class Question(db.Model):
  __tablename__ = "question"
  question_id = db.Column(db.Integer, primary_key=True)
  right_answer = db.Column(db.Integer)
  other_choice_id1 = db.Column(db.Integer)
  other_choice_id2 = db.Column(db.Integer)
  other_choice_id3 = db.Column(db.Integer)
  difficulty = db.Column(db.Integer)

class QuizQuestion(db.Model):
  __tablename__ = "quiz_question"
  quiz_id = db.Column(db.Integer)
  question_id = db.Column(db.Integer)
  id = db.Column(db.Integer, primary_key=True)

class UserAnswer(db.Model):
  __tablename__ = "user_answer"
  user_id = db.Column(db.Integer)
  question_id = db.Column(db.Integer)
  choice_id = db.Column(db.Integer)
  id = db.Column(db.Integer, primary_key=True)


def get_quizes(id):
  session = Session()
  session.query(Quiz).filter_by(quiz_id=id).first()