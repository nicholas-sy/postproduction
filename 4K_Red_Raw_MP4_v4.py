import sys, cv2, os
import numpy as np
from PIL import Image, ImageEnhance
from os.path import isfile, join

directory_main = 'E:/4K_TIFF/EXT/'
directory_contrast = 'E:/4K_TIFF/EXT/contrast/'
directory_proxy = 'E:/4K_TIFF/EXT/proxy/'

def adjust_contrast(input_contrast, output_contrast, factor_contrast):
    image = Image.open(input_contrast)
    enhancer_object = ImageEnhance.Contrast(image)
    out = enhancer_object.enhance(factor_contrast)
    out.save(output_contrast)

def adjust_color(input_color, output_color, factor_color):
    image = Image.open(input_color)
    enhancer_object = ImageEnhance.Color(image)
    out = enhancer_object.enhance(factor_color)
    out.save(output_color)

def frames_to_video(pathIn, pathOut, fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]

    for i in range(len(files)):
        filename=pathIn + files[i]
        #reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        #inserting the frames into an image array
        frame_array.append(img)

    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()

file_start = 'V1-0002_PyTest_4K_Flat00'
frame_start = 350250
frame_end = 351072

for i in range(frame_start, frame_end):

    adjust_contrast(directory_main + file_start + str(i) + '.tif',
                    directory_contrast + file_start + str(i) + '_contrast.jpg',
                    1.3)
    adjust_color(directory_contrast + file_start + str(i) + '_contrast.jpg',
                 directory_proxy + file_start + str(i) + '_proxy.jpg',
                 1.1)

frames_to_video(directory_proxy, directory_proxy + file_start + '_proxy.avi', 24)
