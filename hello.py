from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"


@app.route("/quiz/<int:quiz_id>", method=["GET"])
def quiz(quiz_id: int):
  if request.method == "GET":
    """
    input: quiz_id,
    output: [
      question_id: {
        description: "",
        image: "",
        choices: [
          {name: "doodle", choice_id: 123},
        ]
      },
    ]
    """
    pass


@app.route("user/<int:user_id>/quiz", method=["GET"])
def user_quiz_info(user_id: int):
    if request.method == "GET":
      """
      [quiz_id]
      """
      pass
    


@app.route("user/<int:user_id>/quiz/<int:quiz_id>", method=["POST"])
def user_take_quiz(user_id: int, quiz_id: int):
  if request.method == "POST":
    """
    user_answer
    request_body = {
      question_id: choice_id
    }
    """
    pass
  elif request.method == "GET":
    """
    response_body = {
      question_id: {
        choices: [{1234, "doodle"}, {245, "golden retriever"}, ]
        right_answer: [],
        chosen_answer: [],
      },
      score: ??,
    }
    
    """
