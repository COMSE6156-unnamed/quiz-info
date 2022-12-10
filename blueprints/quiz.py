import requests
from flask import Blueprint, request, Response, render_template, url_for
from utils.exts import db
from utils.model import Question, QuizQuestion, Quiz
from utils.add_question import add_question
from utils.add_quiz import add_quiz
from utils.quiz_utils import format_question
import json

bp = Blueprint("quiz", __name__, url_prefix="/quiz")


@bp.route("/", methods=["GET"])
def all_quiz():
    if request.method == "GET":
        content = []
        for quiz in db.session.query(Quiz).all():
            section = {"quiz_id": quiz.quiz_id, "quiz_content": []}

            for question in db.session.query(Question).join(QuizQuestion,
                                                            QuizQuestion.question_id == Question.question_id) \
                    .filter_by(quiz_id=quiz.quiz_id):
                section["quiz_content"].append(format_question(question))
            content.append(section)
        return Response(json.dumps(content), status=200, content_type="application/json")


@bp.route("/<quiz_id>", methods=["GET"])
def get_quiz(quiz_id: str):
    if request.method == "GET":
        """
        input: quiz_id,
        output: [
            {question_id: "", 
             question_type: "",
             choice_type: "",
             description: "",
             content: "",
             answer: "",
             difficulty: ""
             }, ...
        ]
        """
        content = []
        for question in db.session.query(Question).join(QuizQuestion, QuizQuestion.question_id == Question.question_id) \
                .filter_by(quiz_id=quiz_id):
            content.append(format_question(question))
        return Response(json.dumps(content), status=200, content_type="application/json")


@bp.route("/add-question", methods=["GET", "POST"])
def add_question_to_db():
    if request.method == "GET":
        # direct to the add-question page
        return render_template("add_question.html")
    elif request.method == "POST":
        # add q-nums question to db
        q_type = int(request.form['q-type'])
        q_num = int(request.form['q-nums'])
        ret = add_question(q_type, q_num)
        if ret != 0:
            return "<h2>Failed!</h2> <a href='/quiz/add-question'>back<a>"
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


@bp.route("/take-quiz", methods=["GET", "POST"])
def take_quiz_home():
    if request.method == "GET":
        # direct to the add-question page
        return render_template("take_quiz_home.html")
    elif request.method == "POST":
        user_id = request.form['user-id']
        quiz_id = request.form['quiz-id']
        questions = requests.get(url_for("quiz.get_quiz", quiz_id=quiz_id, _external=True)).json()
        content = {
            "user_id": user_id,
            "quiz_id": quiz_id,
            "questions": questions
        }
        return render_template("take_quiz_main.html", content=content)

