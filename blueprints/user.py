from flask import Blueprint, request, Response
from utils.exts import db
from utils.model import Question, UserAnswer, Quiz
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
        user_answer
        request_body = {
          question_id: 1,
          choice_id: 2
        }
        """
        request_body = json.loads(request.json)
        question_id = int(request_body["question_id"])
        choice_id = int(request_body["choice_id"])
        user_answer = UserAnswer(user_id, quiz_id, question_id, choice_id)
        db.session.add(user_answer)
        db.session.commit()
        return "success"

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
                "choices": [
                    {"id": question.right_answer_id, "name": ""},
                    {"id": question.other_choice_id1, "name": ""},
                    {"id": question.other_choice_id2, "name": ""},
                    {"id": question.other_choice_id3, "name": ""}
                ],
                "right_answer": question.right_answer_id,
                "chosen_answer": user_answer.choice_id
            }
        if content:
            content["score"] = 0
        return Response(json.dumps(content), status=200, content_type="user_take_quiz.json")
