import os

from flask import Flask, render_template_string
from Utils import SCORES_FILE_NAME

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

@app.route('/')
def score_server():
    current_score = get_score()

    if current_score is None:
        return render_template_string(error_template)
    return render_template_string(html_template, score=current_score)

if __name__ == '__main__':
    app.run()