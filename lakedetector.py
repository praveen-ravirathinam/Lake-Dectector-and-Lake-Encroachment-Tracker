#lake finder for satellite images
#input format : $python3 <prog_name>.py -i <image1>.png -c <color> -n <numberofregions>
#example : $ python3 lakedetector.py -i sat1.png -c green -n 2

import sys
import cv2 as cv
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Argument Parser for Command Line args')
parser.add_argument('-i',dest='input_image', type=str, help='Required Input Image Old')
parser.add_argument('-c',dest='color', type=str, nargs='?', help='Optional Color Old')
parser.add_argument('-n',dest='num_lakes', type=int, nargs='?', default=2, help='Optional Number of lakes default = 2')
args = parser.parse_args()
input_image = args.input_image
color = args.color
num = args.num_lakes
input_image_name = input_image[:-4]

# Color of a lake [blue green red]
if color == 'green' : 
    BGR = np.array([85, 105, 90])#green
elif color == 'black' :
    BGR = np.array([20, 25, 20])#black
else:
    BGR = np.array([70, 90, 70])#default

upper = BGR + 10
lower = BGR - 100

# Reads image from disk
def read_image(source='input.png'):
    return cv.imread(source)

# limits the image based on two boundaries
def make_binary(image):
    return cv.inRange(image.copy(), lower, upper)

#
def find_contours(bin_image):
    (contours_list, hierarchy) = cv.findContours(bin_image.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    print("{} contours are present" .format((len(contours_list))))
    return contours_list

def get_top_contours(contours_list):
    copy = contours_list.copy()
    copy.sort(key=len, reverse=True)
    top_contours_dict={}
    for x in range(num):
        top_contours_dict[x]=copy[x]    
    top_contours_list=[v for v in top_contours_dict.values()]
    return top_contours_list

def top_contours(input_image):
    image = read_image(input_image)
    image2 = read_image(input_image)
    binary_image = make_binary(image)
    #cv.imwrite('output_binary_'+input_image_name+'.png',binary_image)
    contours_list = find_contours(binary_image)
    #cv.drawContours(image2, contours_list, -1, (0, 0, 255), 1)
    #cv.imwrite('output_allcontours_'+input_image_name+'.png',image2)  
    top_contours= get_top_contours(contours_list) 
    return top_contours

# draw contours on the image
def draw_contours(contours_list, image):
    cv.drawContours(image, contours_list, -1, (0, 0, 255), 1)

def make_output(image):
    cv.imwrite('output_'+input_image_name+'.png',image)

if __name__ == "__main__":

    top_contours_input_image= top_contours(input_image)
    output_image= read_image(input_image)
    draw_contours(top_contours_input_image,output_image)
    make_output(output_image)   
