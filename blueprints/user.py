from flask import Blueprint, request, Response
from utils.exts import db
from utils.model import Question, UserAnswer, Quiz, QuizQuestion
import json

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/<int:user_id>/quiz", methods=["GET"])
def user_quiz_info(user_id: int):
    if request.method == "GET":
        """
        [quiz_id]
        """
        content = []
        for quiz in db.session.query(Quiz) \
                .join(UserAnswer, UserAnswer.quiz_id == Quiz.quiz_id) \
                .filter(UserAnswer.user_id == user_id):
            content.append(quiz.quiz_id)
        return Response(json.dumps(content), status=200, content_type="user_quiz_info.json")


@bp.route("/<int:user_id>/quiz/<int:quiz_id>", methods=["POST", "GET"])
def user_take_quiz(user_id: int, quiz_id: int):
    if request.method == "POST":
        """
        request_body = {
          question_id: []
        }

        response_body = {

        }

        """
        for question_id in request.form.keys():
            answer_list = request.form.getlist(question_id)
            answer = '\n'.join(answer_list)
            user_answer = UserAnswer(user_id, quiz_id, int(question_id), answer)
            db.session.add(user_answer)
        db.session.commit()

        resp = {"right_answers": {}}
        score = 0
        for question in db.session.query(Question) \
                    .join(QuizQuestion, QuizQuestion.question_id == Question.question_id) \
                    .filter(QuizQuestion.quiz_id == quiz_id):
          right_answer = question.answer.split('\n')
          resp["right_answers"][question.question_id] = right_answer
          if set(right_answer) == set(request.form.getlist(question_id)):
            score += 1
        
        resp["score"] = score / len(resp["right_answers"]) * 100
        return Response(json.dumps(resp), status=200)

    elif request.method == "GET":
        """
        response_body = {
          question_id: {
            choices: [{id: 1234, name: "doodle"}, {id: 245, name: "golden retriever"}, ]
            right_answer: [],
            chosen_answer: [],
          },
          score: ??,
        }

        """
        content = {}
        for user_answer, question in db.session.query(UserAnswer, Question) \
                .join(Question, UserAnswer.question_id == Question.question_id) \
                .filter(UserAnswer.user_id == user_id, UserAnswer.quiz_id == quiz_id):
            content[question.question_id] = {
                "description": question.description,
                "content": question.content,
                "right_answer": question.answer,
                "user_answer": user_answer.user_answer
            }
        if content:
            content["score"] = 0
        return Response(json.dumps(content), status=200, content_type="user_take_quiz.json")
