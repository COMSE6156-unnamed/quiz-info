# Dog-info API related
DOG_INFO_API_URL = "http://doginfo-env.eba-ui3pwzdu.us-east-1.elasticbeanstalk.com"
DOG_ALL_URL = DOG_INFO_API_URL + "/dogs"
DOG_ONE_URL = DOG_ALL_URL + "/{}"
DOG_CATEGORIES_URL = DOG_ONE_URL + "/categories"
DOG_ORIGINS_URL = DOG_ONE_URL + "/origins"
DOG_SIZE_URL = DOG_ONE_URL + "/size"
DOG_IMAGE_URL = DOG_ONE_URL + "/image_url"
DOG_PRONUNCIATION_URL = DOG_ONE_URL + "/pronunciation"

# Add-question related
# q_type
IMG_TO_NAME_TYPE = 0
IMG_TO_SIZE_TYPE = 1
IMG_TO_ORIGIN_TYPE = 2
IMG_TO_CATEGORY_TYPE = 3
NAME_TO_IMG_TYPE = 4
NAME_TO_SIZE_TYPE = 5
NAME_TO_ORIGIN_TYPE = 6
NAME_TO_CATEGORY_TYPE = 7
# c_type
SINGLE_CHOICE_TYPE = 0
MULTIPLE_CHOICE_TYPE = 1
# q_category
IMG_QUESTIONS = [IMG_TO_NAME_TYPE, IMG_TO_ORIGIN_TYPE, IMG_TO_SIZE_TYPE, IMG_TO_CATEGORY_TYPE]
NAME_QUESTIONS = [NAME_TO_IMG_TYPE, NAME_TO_SIZE_TYPE, NAME_TO_ORIGIN_TYPE, NAME_TO_CATEGORY_TYPE]
ALL_QUESTIONS = IMG_QUESTIONS + NAME_QUESTIONS
# description corresponds to q_type
DESCRIPTION_MAP = {
    IMG_TO_NAME_TYPE: {
        SINGLE_CHOICE_TYPE: "Choose the name matches the dog shown in the below image.\n"
    },
    IMG_TO_SIZE_TYPE: {
        SINGLE_CHOICE_TYPE: "Choose the size matches the dog shown in the below image.\n"
    },
    IMG_TO_ORIGIN_TYPE: {
        SINGLE_CHOICE_TYPE: "Choose the origin matches the dog shown in the below image.\n",
        MULTIPLE_CHOICE_TYPE: "Choose ONE OR MORE origins match the dog shown in the below image.\n"
    },
    IMG_TO_CATEGORY_TYPE: {
        SINGLE_CHOICE_TYPE: "Choose the category matches the dog shown in the below image.\n",
        MULTIPLE_CHOICE_TYPE: "Choose ONE OR MORE categories match the dog shown in the below image.\n"
    },
    NAME_TO_IMG_TYPE: {
        SINGLE_CHOICE_TYPE: "Choose the image of {}.",
    },
    NAME_TO_SIZE_TYPE: {
        SINGLE_CHOICE_TYPE: "Choose the size of {}."
    },
    NAME_TO_ORIGIN_TYPE: {
        SINGLE_CHOICE_TYPE: "Choose the origin of {}.",
        MULTIPLE_CHOICE_TYPE: "Choose the origin(s) of {}. There may be ONE OR MORE right answers."
    },
    NAME_TO_CATEGORY_TYPE: {
        SINGLE_CHOICE_TYPE: "Choose the category of {}.",
        MULTIPLE_CHOICE_TYPE: "Choose the category(s) of {}. There may be ONE OR MORE right answers."
    }
}
# choice num corresponds to q_type
CHOICE_NUM_MAP = {
    IMG_TO_NAME_TYPE: 4,
    IMG_TO_ORIGIN_TYPE: 4,
    IMG_TO_SIZE_TYPE: 4,
    IMG_TO_CATEGORY_TYPE: 4,
    NAME_TO_IMG_TYPE: 4,
    NAME_TO_SIZE_TYPE: 4,
    NAME_TO_ORIGIN_TYPE: 4,
    NAME_TO_CATEGORY_TYPE: 4
}

# error message
ERROR_MSG = "error"
