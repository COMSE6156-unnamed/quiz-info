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
    description = db.Column(db.String(256))
    img_url = db.Column(db.String(256))
    right_answer_id = db.Column(db.Integer)
    other_choice_id1 = db.Column(db.Integer)
    other_choice_id2 = db.Column(db.Integer)
    other_choice_id3 = db.Column(db.Integer)
    difficulty = db.Column(db.Integer)

    def __init__(self, question_id, description, img_url, right_answer_id, other_choice_id1,
                 other_choice_id2, other_choice_id3, difficulty):
        self.question_id = question_id
        self.description = description
        self.img_url = img_url
        self.right_answer_id = right_answer_id
        self.other_choice_id1 = other_choice_id1
        self.other_choice_id2 = other_choice_id2
        self.other_choice_id3 = other_choice_id3
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
    choice_id = db.Column(db.Integer)

    def __init__(self, user_id, quiz_id, question_id, choice_id):
        self.user_id = user_id
        self.quiz_id = quiz_id
        self.question_id = question_id
        self.choice_id = choice_id
