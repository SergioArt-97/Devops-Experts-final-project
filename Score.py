import os
from Utils import SCORES_FILE_NAME

def add_score(difficulty):
    points = (difficulty * 3) + 5

    try:
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, "r") as score_file:
                current_score = int(score_file.read().strip() or 0)
        else:
            current_score = 0

    except (FileNotFoundError, ValueError):
        current_score = 0

    new_score = current_score + points

    with open(SCORES_FILE_NAME, "w") as score_file:
        score_file.write(str(new_score))