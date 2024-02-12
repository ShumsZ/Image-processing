from PIL import Image

image = Image.open('2194.jpg')

user_selection = input('Choose cool or warm. For Cool, type "C". For Warm, type "W":  ')


def cool(img):
    red, green, blue = img.split()

    less_red = red.point(lambda pix: pix * 0.7)
    less_green = green.point(lambda pix: pix * 0.7)

    cool_img = Image.merge('RGB', (less_red, less_green, blue))
    return cool_img


def warm(img):
    red, green, blue = img.split()

    less_blue = blue.point(lambda pix: pix * 0.7)
    less_green = green.point(lambda pix: pix * 0.7)

    warm_img = Image.merge('RGB', (red, less_green, less_blue))
    return warm_img


if user_selection == 'W':
    image_tone = warm(image)
    image_tone.show()
elif user_selection == 'C':
    image_tone = cool(image)
    image_tone.show()
else:
    print('select an option!')
