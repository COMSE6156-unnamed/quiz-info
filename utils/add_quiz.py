import random
from utils.exts import db
from utils.model import Question, Quiz, QuizQuestion


def add_quiz(num: int) -> None:
    """
    Add <num> quiz into the database. Each quiz is generated by selecting ten random questions from question table.
    :param num: # of quiz to add.
    :return: None
    """
    question_id_list = list(db.session.query(Question.question_id))

    for i in range(num):
        quiz = Quiz(None, -1)
        db.session.add(quiz)
        db.session.flush()
        db.session.refresh(quiz)
        idx_tuple_list = random.sample(question_id_list, 10)
        for idx_tuple in idx_tuple_list:
            quiz_question = QuizQuestion(None, quiz.quiz_id, idx_tuple[0])
            db.session.add(quiz_question)
            db.session.commit()
