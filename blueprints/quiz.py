from flask import Blueprint, request, Response
from utils.exts import db
from utils.model import Question, QuizQuestion
import json

bp = Blueprint("quiz", __name__, url_prefix="/quiz")


@bp.route("/<int:quiz_id>", methods=["GET"])
def quiz(quiz_id: int):
    if request.method == "GET":
        """
        input: quiz_id,
        output: {
          question_id: {
            description: "",
            image: "",
            choices: [
              {name: "doodle", choice_id: 123},
            ]
          },
        }
        """
        content = {}
        for question in db.session.query(Question).join(QuizQuestion, QuizQuestion.question_id == Question.question_id) \
                .filter_by(quiz_id=quiz_id):
            content[question.question_id] = {
                "description": "",
                "image": "",
                "choices": [
                    {"name": "", "choice_id": question.right_answer_id},
                    {"name": "", "choice_id": question.other_choice_id1},
                    {"name": "", "choice_id": question.other_choice_id2},
                    {"name": "", "choice_id": question.other_choice_id3}
                ]
            }
        return Response(json.dumps(content), status=200, content_type="quiz.json")
