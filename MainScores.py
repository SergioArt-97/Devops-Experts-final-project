import os
from Score import add_score

from flask import Flask, render_template_string
from Utils import SCORES_FILE_NAME

def ensure_scores_file():
    if not os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, "w") as score_file:
            score_file.write("0")

ensure_scores_file()

app = Flask(__name__)

def get_score():
    try:
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, "r") as score_file:
                return int(score_file.read().strip() or 0)
        return 0

    except (FileNotFoundError, ValueError):
        current_score = 0

error_template = """
<html>
    <head>
        <title>Scores Game</title>
    </head>
    <body>
        <h1><div id="score" style="color:red">ERROR</div></h1>
    </body>
</html>
"""

html_template = """
<html>
    <head>
        <title>Scores Game</title>
    </head>
    <body>
        <h1>The score is <div id="score">{{ score }}</div></h1>
    </body>
</html>
"""

@app.route('/add_score/<int:difficulty>', methods=['POST'])
def add_score_route(difficulty):
    add_score(difficulty)  # Update the score based on difficulty
    return f"Score updated! New score added based on difficulty {difficulty}.", 200


@app.route('/')
def score_server():
    current_score = get_score()

    if current_score is None:
        return render_template_string(error_template)
    return render_template_string(html_template, score=current_score)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)