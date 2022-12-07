import utils.cons as cons
from utils.exts import db
from utils.model import Question, UserAnswer, Quiz, QuizQuestion, UserQuiz

def format_question(question_entry) -> dict:
  entry = {
            "question_id": question_entry.question_id,
            "description": question_entry.description,
            "choices": question_entry.content.split('\n'),
            "answers": question_entry.answer.split('\n'),
            "difficulty": question_entry.difficulty,
          }
  if question_entry.image_url:
    entry["image_url"] = question_entry.image_url
  return entry

def user_take_quiz_resp(user_id: int, quiz_id: int) -> dict:
    content = {}
    for user_answer, question in db.session.query(UserAnswer, Question) \
          .join(Question, UserAnswer.question_id == Question.question_id) \
          .filter(UserAnswer.user_id == user_id, UserAnswer.quiz_id == quiz_id):
      content[question.question_id] = {
          "description": question.description,
          "choices": question.content.split("\n"),
          "right_answer": question.answer.split("\n"),
          "user_answer": user_answer.user_answer.split("\n")
      }
    for user_quiz in db.session.query(UserQuiz) \
        .filter(UserQuiz.user_id == user_id, UserQuiz.quiz_id == quiz_id):
      content["score"] = user_quiz.score
    return content