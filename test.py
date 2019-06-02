# -*- coding: utf-8 -*-
from PIL import Image
im = Image.open('GUI/wall_photo.png', 'r')
im_alpha = im.convert('RGBA')
pixels = list(im.getdata())
#pix_val = list(im.getdata())
#print(pix_val_flat)
temp_list = []
fin = []
count = 0
print('1')
cot = 0
for rgb in pixels:
    print(cot)
    count += 1
    temp_list.append(rgb)
    if count == 4:
        fin.append(temp_list)
        count = 0
    cot += 1
print('1')
print(fin)

from PIL import Image
import numpy as np


pixels = [
   [(54, 54, 54,0), (232, 23, 93,0), (71, 71, 71,0), (168, 167, 167,0)],
   [(204, 82, 122,0), (54, 54, 54,0), (168, 167, 167,0), (232, 23, 93,0)],
   [(71, 71, 71,0), (168, 167, 167,0), (54, 54, 54,0), (204, 82, 122,0)],
   [(168, 167, 167,0), (204, 82, 122,0), (232, 23, 93,0), (54, 54, 54,0)]
]

# Convert the pixels into an array using numpy
array = np.array(fin, dtype=np.uint8)

# Use PIL to create an image from the new array of pixels
new_image = Image.fromarray(array)
new_image.save('new.png')




def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()