from utils.exts import db


class Quiz(db.Model):
    __tablename__ = "quiz"
    quiz_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    difficulty = db.Column(db.Integer)

    def __init__(self, quiz_id, difficulty):
        self.quiz_id = quiz_id
        self.difficulty = difficulty


class Question(db.Model):
    __tablename__ = "question"
    question_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    q_type = db.Column(db.Integer)
    c_type = db.Column(db.Integer)
    description = db.Column(db.String(1024))
    content = db.Column(db.String(1024))
    answer = db.Column(db.String(256))
    difficulty = db.Column(db.Integer)

    def __init__(self, question_id, q_type, c_type, description, content, answer, difficulty):
        self.question_id = question_id
        self.q_type = q_type
        self.c_type = c_type
        self.description = description
        self.content = content
        self.answer = answer
        self.difficulty = difficulty


class QuizQuestion(db.Model):
    __tablename__ = "quiz_question"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quiz_id = db.Column(db.Integer)
    question_id = db.Column(db.Integer)

    def __init__(self, quiz_question_id, quiz_id, question_id):
        self.id = quiz_question_id
        self.quiz_id = quiz_id
        self.question_id = question_id


class UserAnswer(db.Model):
    __tablename__ = "user_answer"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    quiz_id = db.Column(db.Integer)  # Different quiz have same question
    question_id = db.Column(db.Integer)
    user_answer = db.Column(db.String(256))

    def __init__(self, user_id, quiz_id, question_id, user_answer):
        self.user_id = user_id
        self.quiz_id = quiz_id
        self.question_id = question_id
        self.user_answer = user_answer
