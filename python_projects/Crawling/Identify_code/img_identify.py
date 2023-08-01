#  -*- UTF-8 -*- #
"""
@filename:img_identify.py
@author:Anza
@time:2023-08-01
"""


import pytesseract
from PIL import Image


# def modify_img(img):
#     img.convert('L')
#     threshold = 127
#     table = []
#     for i in range(256):
#         if i < threshold:
#             table.append(0)
#         else:
#             table.append(1)
#
#     img = img.point(table, '1')
#     img.show()
#     return img


if __name__ == '__main__':
    image = Image.open('code.jpg')

    # image = modify_img(image)
    image = image.convert('L')
    # image.show()
    threshold = 140
    func = lambda x: 0 if x < threshold else 1
    image = image.point(func, '1')
    image.show()

    result = pytesseract.image_to_string(image, lang="eng")
    print(result)
