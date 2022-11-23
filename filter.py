from PIL import Image, ImageFilter
from cs50 import get_int, get_string
image_path = get_string("write down file path ")
n = get_int("how much blur do you want? ")
before = Image.open(image_path)
after = before.filter(ImageFilter.BoxBlur(n))
nome_file = get_string("nome del nuovo file? ")
after.save(nome_file + ".jpg")
