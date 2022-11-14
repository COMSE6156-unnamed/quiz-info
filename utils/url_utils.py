import utils.cons as cons

def get_dog_image_url(dog_id: int) -> str:
  return cons.DOG_IMAGE_URL.format(dog_id)