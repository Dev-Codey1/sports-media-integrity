import imagehash
from PIL import Image

def get_perceptual_hash(image_path):
    # Ye image ki structure ko scan karta hai, pixels ko nahi
    hash_value = imagehash.phash(Image.open(image_path))
    return str(hash_value)

# Example use:
# original = get_perceptual_hash('clip_frame_1.jpg')
# print(f"Permanent Digital ID: {original}")
