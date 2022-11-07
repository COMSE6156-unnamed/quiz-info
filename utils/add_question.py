import random
from utils.exts import db
from utils.model import Question
import utils.cons as cons
import requests


def add_image_question(num: int) -> None:
    """
    Add <num> questions, each of them show an image and user need to choose a right answer from four choices.
    :param num: # of questions
    :return: None
    """
    idx_list = random.sample(range(1, 51), num)  # upper bound may need to be changed
    for idx in idx_list:
        image_url = requests.get(cons.DOG_IMAGE_URL.format(idx)).json()['image_url']
        wrong_list = random.sample([*range(1, idx), *range(idx + 1, 51)], 3)
        question = Question(None, "Please choose the name matches the dog shown in the below image:", image_url, idx,
                            wrong_list[0], wrong_list[1], wrong_list[2], -1)
        db.session.add(question)
        db.session.commit()
