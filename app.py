from flask import Flask, render_template
from flask_migrate import Migrate
import config
from utils.exts import db
from blueprints import quiz_bp, user_bp

# app config
app = Flask(__name__)
app.config.from_object(config)

# DB config
db.init_app(app)  # Init DB
migrate = Migrate(app, db)  # DB Version Control

# Blueprints
app.register_blueprint(quiz_bp)  # Quiz related API
app.register_blueprint(user_bp)  # User related API


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
