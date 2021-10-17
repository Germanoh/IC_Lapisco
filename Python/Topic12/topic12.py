'''
Opens a text file turns the image on it grayscale and display on screen
'''

import cv2 as cv

# tries to open a text file that contains the image content
# and saves it on a variable
try:
    with open("pixel_values.txt", 'r') as file:
        content = file.read()
except:
    print("Couldn't open the file")

