import sys
from PIL import Image

orig_img_name = sys.argv[1]

# TODO: Check if file is indeed of type PNG

grayscaled_img = Image.open(orig_img_name).convert('LA')
grayscaled_img_name = 'grayscaled-' + orig_img_name
grayscaled_img.save('gray.png')
