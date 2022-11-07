from flask import Blueprint, request, Response, render_template
from utils.exts import db
from utils.model import Question, QuizQuestion
from utils.add_question import add_image_question
from utils.add_quiz import add_quiz
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
                "description": question.description,
                "image": question.img_url,
                "choices": [
                    {"name": "", "choice_id": question.right_answer_id},
                    {"name": "", "choice_id": question.other_choice_id1},
                    {"name": "", "choice_id": question.other_choice_id2},
                    {"name": "", "choice_id": question.other_choice_id3}
                ]
            }
        return Response(json.dumps(content), status=200, content_type="quiz.json")


@bp.route("/add-question", methods=["GET", "POST"])
def add_question_to_db():
    if request.method == "GET":
        # direct to the add-question page
        return render_template("add_question.html")
    elif request.method == "POST":
        # add q-nums question to db
        add_image_question(int(request.form['q-nums']))
        return "<h2>success</h2> <a href='/quiz/add-question'>back<a>"


@bp.route("/add-quiz", methods=["GET", "POST"])
def add_quiz_to_db():
    if request.method == "GET":
        # direct to the add-question page
        return render_template("add_quiz.html")
    elif request.method == "POST":
        # add q-nums question to db
        add_quiz(int(request.form['q-nums']))
        return "<h2>success</h2> <a href='/quiz/add-quiz'>back<a>"
