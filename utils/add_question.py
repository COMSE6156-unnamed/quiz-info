import random
from utils.exts import db
from utils.model import Question
from utils.url_utils import get_dog_image_url
import utils.cons as cons
import requests


def get_dog_id_range() -> list:
    """
    Get all dogs' id as a list.
    :return: List
    """
    dog_list = requests.get(cons.DOG_ALL_URL).json()
    res = []
    for dog in dog_list:
        res.append(dog["id"])
    return res


def get_dog_info_range(q_type: int) -> list:
    """
    Get the dog info corresponds to q_type
    :param q_type: type of the question
    :return: dog info list
    """
    dog_list = requests.get(cons.DOG_ALL_URL).json()
    info_set = set()

    if q_type == cons.IMG_TO_NAME_TYPE:
        for dog in dog_list:
            if dog['name']:
                info_set.add(dog['name'])
    elif q_type == cons.IMG_TO_SIZE_TYPE or q_type == cons.NAME_TO_SIZE_TYPE:
        for dog in dog_list:
            if dog['size']['name']:
                info_set.add(dog['size']['name'])
    elif q_type == cons.IMG_TO_ORIGIN_TYPE or q_type == cons.NAME_TO_ORIGIN_TYPE:
        for dog in dog_list:
            for origin in dog['origins']:
                if origin:
                    info_set.add(origin['name'])
    elif q_type == cons.IMG_TO_CATEGORY_TYPE or q_type == cons.NAME_TO_CATEGORY_TYPE:
        for dog in dog_list:
            for category in dog['categories']:
                if category:
                    info_set.add(category['name'])
    elif q_type == cons.NAME_TO_IMG_TYPE:
        for dog in dog_list:
            url = dog['image_url']
            if url and url.startswith("http"):
                info_set.add(url)
    else:
        pass
    return list(info_set)


def create_description(q_type: int, c_type: int, dog: dict) -> str:
    """
    create the description corresponds to q_type and c_type
    if the the question is in cons.IMG_QUESTIONS, do not add anything to the description
    :param q_type: question type
    :param c_type: choice type
    :param dog: dog instance
    :return: string of description
    """
    description = cons.DESCRIPTION_MAP[q_type][c_type]
    if q_type in cons.NAME_QUESTIONS:
        name = dog['name']
        if name:
            description = description.format(name)
        else:
            return cons.ERROR_MSG
    
    return description


def create_answer_list(q_type: int, dog: dict) -> list:
    """
    create the answer list corresponds to q_type
    :param q_type: question type
    :param dog: dog instance
    :return: description string
    """
    answer_list = []
    if q_type == cons.IMG_TO_NAME_TYPE:
        answer_list = [dog['name']]
    elif q_type == cons.IMG_TO_SIZE_TYPE or q_type == cons.NAME_TO_SIZE_TYPE:
        answer_list = [dog['size']['name']]
    elif q_type == cons.IMG_TO_ORIGIN_TYPE or q_type == cons.NAME_TO_ORIGIN_TYPE:
        answer_list = [origin['name'] for origin in dog['origins']]
    elif q_type == cons.IMG_TO_CATEGORY_TYPE or q_type == cons.NAME_TO_CATEGORY_TYPE:
        answer_list = [category['name'] for category in dog['categories']]
    elif q_type == cons.NAME_TO_IMG_TYPE:
        # TODO: change the url to an API path
        url = dog['image_url']
        if url and url.startswith("http"):
            answer_list = [url]
    else:
        pass

    return answer_list


def create_answer(answer_list: list) -> str:
    """
    create the answer string corresponds to answer_list
    :param answer_list: list of answers
    :return: answer string
    """
    return '\n'.join(answer_list)


def create_content(dog_info: list, answer_list: list, choice_num: int) -> str:
    """
    Create the content of the question
    :param dog_info: all required info
    :param answer_list: answer list
    :param choice_num: # of choices
    :return: a content String
    """
    remain_info = dog_info.copy()
    # remove answers
    for answer in answer_list:
        remain_info.remove(answer)
    choice_list = answer_list
    while len(choice_list) < choice_num:
        wrong_dog_info = random.choice(remain_info)
        choice_list.append(wrong_dog_info)
        remain_info.remove(wrong_dog_info)
    random.shuffle(choice_list)
    content = '\n'.join(choice_list)
    return content


def get_choice_num(q_type: int) -> int:
    """
    get the numer of choices corresponds to q_type
    :param q_type: question type
    :return: # of choices
    """
    return cons.CHOICE_NUM_MAP[q_type]


def get_choice_type(answer_list: list) -> int:
    """
    get the type of choices corresponds to answer_list
    :param answer_list: list of answers
    :return: type of choice
    """
    if len(answer_list) == 1:
        return 0
    else:
        return 1


def add_question(q_type_input: int, q_num: int) -> int:
    """
    Add <q_num> questions of <q_type>.
    :param q_type_input: type of question
    :param q_num: # of questions
    :return: 0 Success 1 Fail
    """
    dog_id_all = get_dog_id_range()
    dog_info_all = None
    cnt = 0
    while cnt < q_num:
        if q_type_input < 0:  # random question type
            q_type = random.choice(cons.ALL_QUESTIONS)
            dog_info_all = get_dog_info_range(q_type)
        else:
            q_type = q_type_input
            if not dog_info_all:
                dog_info_all = get_dog_info_range(q_type)

        # query a random dog
        dog_id = random.choice(dog_id_all)
        dog = requests.get(cons.DOG_ONE_URL.format(dog_id)).json()
        if "error" in dog:
            continue

        # create answer
        answer_list = create_answer_list(q_type, dog)
        if not answer_list:
            continue
        answer = create_answer(answer_list)

        # create choice info
        choice_num = get_choice_num(q_type)
        c_type = get_choice_type(answer_list)

        # create description
        description = create_description(q_type, c_type, dog)
        if description == cons.ERROR_MSG:
            continue

        # create content
        content = create_content(dog_info_all, answer_list, choice_num)

        # create image_url
        image_url = None if q_type not in cons.IMG_QUESTIONS else get_dog_image_url(dog_id)

        # create question instance
        question = Question(None, q_type, c_type, description, content, answer, -1, image_url)

        # add instance to db
        db.session.add(question)
        cnt += 1

    # commit transactions
    db.session.commit()
    return 0
