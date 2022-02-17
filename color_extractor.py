from PIL import Image
import numpy as np

img = Image.open("test.jpg")  # IMAGE PATH GOES HERE # . upload any image you would like to use to the directory that contains your code

width, height = img.size  # assign the number of pixels in the x axis to width and ones in y axis to height

# initialise the count for each colour to 0.
white_count = 0
black_count = 0
red_count = 0
blue_count = 0
green_count = 0

# The idea here is that upon meeting certain conditions listed below, the following for loop decides which pixels are predominantly red, green, blue or whether they are white or black
for y in range(height):
    for x in range(width):
        r, g, b = img.getpixel((x, y))
        if r == 255 and g == 255 and b == 255:
            white_count += 1
        if r + b + g <= 15:
            black_count += 1
        if r > g and r > b and r + b + g > 15:  # if the value of red is greater than blue and green and it isn't considered to be black
            red_count += 1
        if g > r and g > b and r + b + g > 15:  # if the value of green is greater than blue and red and it isn't considered to be black
            green_count += 1
        if b > r and b > g and r + b + g > 15:  # if the value of blue is greater than red and green and it isn't considered to be black
            blue_count += 1

print(white_count, ' ', black_count, ' ', red_count, ' ', green_count, ' ', blue_count)

# work out proportions of each colour
blue_percent = blue_count / (blue_count + red_count + green_count + black_count + white_count)
red_percent = red_count / (blue_count + red_count + green_count + black_count + white_count)
green_percent = green_count / (blue_count + red_count + green_count + black_count + white_count)
black_percent = black_count / (blue_count + red_count + green_count + black_count + white_count)
white_percent = white_count / (blue_count + red_count + green_count + black_count + white_count)

# set the width and height of output image which will display the proportions of colours
w, h = 1024, 1024

# work out the relative slice of each colour
white_image_slice = white_percent * w
red_image_slice = red_percent * w
green_image_slice = green_percent * w
blue_image_slice = blue_percent * w
black_image_slice = black_percent * w

# print(white_image_slice)

# use numpy to generate the array that wil store the value of the slices appropriately
data = np.zeros((h, w, 3), dtype=np.uint8)
data[0:int(white_image_slice)] = [255, 255, 255]
data[int(white_image_slice):int(white_image_slice) + int(red_image_slice)] = [255, 0, 0]
data[int(white_image_slice) + int(red_image_slice):int(white_image_slice) + int(red_image_slice) + int(
    green_image_slice)] = [0, 255, 0]
data[int(white_image_slice) + int(red_image_slice) + int(green_image_slice):int(white_image_slice) + int(
    red_image_slice) + int(green_image_slice) + int(blue_image_slice)] = [0, 0, 255]
data[int(white_image_slice) + int(red_image_slice) + int(green_image_slice) + int(blue_image_slice):int(
    white_image_slice) + int(red_image_slice) + int(green_image_slice) + int(blue_image_slice) + int(
    black_image_slice)] = [0, 0, 0]
final_img = Image.fromarray(data, 'RGB')

# output the image which displays the relative proportions of each defined colour in the given image
final_img.show()
