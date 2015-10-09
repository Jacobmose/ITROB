#!/usr/bin/env python

import cv2
from QRfuncs import QRfuncs
import numpy as np
from Recognition import Recognition

qr_funcs = QRfuncs()

#qr_funcs.create_qr_image("red",True)
#qr_funcs.decode_qr_code()


recog = Recognition()

image = recog.fetch_image_from_webcam()

lower_blue = np.array([100,100,40])   #Darker Colour
upper_blue = np.array([130,255,255]) #Bright Colour
lower_red = np.array([0,50,50])
upper_red = np.array([20,255,255])
lower_green = np.array([40,80,55])
upper_green = np.array([90,255,255])
lower_yellow = np.array([20,50,50])
upper_yellow = np.array([30,255,255])

yellowbrick = recog.detect_brick(image, lower_yellow, upper_yellow)
bluebrick = recog.detect_brick(image, lower_blue, upper_blue)
greenbrick = recog.detect_brick(image, lower_green, upper_green)
redbrick = recog.detect_brick(image, lower_red, upper_red)



cv2.waitKey(0)


