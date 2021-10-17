'''
Opens an colored image, turn to shades of gray, display on screen and saves it
'''


import cv2 as cv
import numpy as np

def convert_grayscale(image):
    ''' receives a colored image and converts to grayscale using the method
        of taking the mean values of channnels 
        
    ARGS:
        - image: data from image
        - shape: tuple containing width x height
    RETURN:
        - image on grayscale format

    '''
    nRows, nCols = image.shape[0], image.shape[1]

    # return (nRows, nCols)
    new_img = np.zeros((nRows, nCols), dtype=np.uint8)
    print(new_img.dtype)

    for i in range(nRows):
        for j in range(nCols):
            '''first method: average value of pixels''' 
            # px_gray = int((img[i][j][0] + img[i][j][1] + img[i][j][2]) / 3)

            '''second method: channel-dependent luminance perception
               (y = 0.212R + 0.7152G + 0.0722B)
            '''
            # px_blue = 0.0722 * img[i][j][0]
            # px_green = 0.7152 * img[i][j][1]
            # px_red = 0.2126 * img[i][j][2]
            # px_gray = int(px_blue + px_green + px_red)

            '''third method: linear approximation of gamma-correction 
               (y = 0.299R + 0.587G + 0.114B)
            '''
            # px_blue = 0.114 * img[i][j][0]
            # px_green = 0.587 * img[i][j][1]
            # px_red = 0.299 * img[i][j][2]
            # px_gray = int(px_blue + px_green + px_red)

            # new_img[i][j] = px_gray'''

            '''using numpy methods to increase speed and linear approximation of gamma-correction'''
            px_blue = 0.114 * img.item(i, j, 0)
            px_green = 0.587 * img.item(i, j, 1)
            px_red = 0.299 * img.item(i, j, 2)
            px_gray = int(px_blue + px_green + px_red)

            new_img.itemset((i, j), px_gray)


    return new_img

'reads colored image'
img = cv.imread('image.jpg')

'converts the image to shades of grey'
gray_img = convert_grayscale(img)

'display gray image'
cv.imshow('Display gray', gray_img)

key2 = cv.waitKey(0)

'saves gray image'
cv.imwrite('grayscale_image.jpg', gray_img)