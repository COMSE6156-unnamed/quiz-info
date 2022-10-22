from typing import List

class Question:
  def __init__(self, id: int, difficulty, choices : List[int], right_answer: int) -> None:
    self.__id = id
    self.__difficulty = difficulty
    self.__choices = choices
    self.__right_answer = right_answer
  
  def is_right(self, choice):
    return choice == self.__right_answer


class Quiz:
  def __init__(self, questions) -> None:
    self.__questions = questions

  def get_questions(self) -> List[Question]:
    return self.__questions

