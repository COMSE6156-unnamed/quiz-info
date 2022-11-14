import utils.cons as cons

def format_question(question_entry) -> dict:
  entry = {
            "question_id": question_entry.question_id,
            "description": question_entry.description,
            "choices": question_entry.content.split('\n'),
            "answers": question_entry.answer.split('\n'),
            "difficulty": question_entry.difficulty,
          }
  if question_entry.image_url:
    entry["image_url"] = question_entry.image_url
  return entry

