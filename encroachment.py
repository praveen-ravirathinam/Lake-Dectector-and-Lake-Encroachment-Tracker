#encroachment finder for satellite images
#input format : $python3 <prog_name>.py -i <image1>.png -o <image2.png> -co <color> -cn <color> -n <numberofregions>
#example : $ python3 encroachment.py -i sat1.png -o sat2.png -co black -cn green -n 1

import sys
import cv2 as cv
import numpy as np
import argparse

# ArgumentParser
parser = argparse.ArgumentParser(description='Argument Parser for Command Line args')
parser.add_argument('-i',dest='input_old', type=str, help='Required Input Image Old')
parser.add_argument('-o',dest='input_new', type=str, help='Required Input Image new')
parser.add_argument('-co',dest='color_old', type=str, nargs='?', help='Optional Color Old')
parser.add_argument('-cn',dest='color_new', type=str, nargs='?', help='Optional Color New')
parser.add_argument('-n',dest='num_lakes', type=int, nargs='?', default=2, help='Optional Number of lakes ; default = 2')
args = parser.parse_args()
input_image_old = args.input_old
input_image_new = args.input_new
color_old = args.color_old
color_new = args.color_new
num = args.num_lakes
input_image_old_name=input_image_old[:-4]
input_image_new_name=input_image_new[:-4]

#checking if number of lakes is a postive number or none
# if num == None or num <= 0:
#     num=2

# Color of a lake [blue green red]
def color_lake(color):    
    if color == 'green' : 
        BGR = np.array([85, 105, 90])#green
    elif color == 'black' :
        BGR = np.array([20, 25, 20])#black
    else:
         BGR = np.array([70, 90, 70])
    return BGR

BGR_old = color_lake(color_old)
upper_old = BGR_old + 10
lower_old = BGR_old - 100

BGR_new = color_lake(color_new)
upper_new = BGR_new + 10
lower_new = BGR_new - 100

# Reads image from disk
def read_image(source):
    return cv.imread(source)

# limits the image based on two boundaries
def make_binary(image,age="new"):
    raw_image = read_image(image)
    if age == "old":
        return cv.inRange(raw_image, lower_old, upper_old)
    else:
        return cv.inRange(raw_image, lower_new, upper_new)

#find all contours in the image
def find_contours(bin_image):
    (contours_list, hierarchy) = cv.findContours(bin_image.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    print("{} contours are present" .format((len(contours_list))))
    return contours_list

#get the top 2 contours 
def get_top_contours(contours_list):
    copy = contours_list.copy()
    copy.sort(key=len, reverse=True)
    top_contours_dict={}
    for x in range(num):
        top_contours_dict[x]=copy[x]    
    top_contours_list=[v for v in top_contours_dict.values()]
    return top_contours_list
    #return copy[0],copy[1]

# draw contours on the image
def draw_contours_red(contours_list, image):
    cv.drawContours(image, contours_list, -1, (0, 0, 255), 1)

def draw_contours_blue(contours_list, image):
    cv.drawContours(image, contours_list, -1, (255, 0, 0), 1)

#getting top contours
def top_contours(input_image):
    contours_list = find_contours(input_image)
    top_contours= get_top_contours(contours_list) 
    return top_contours

#make output image file
def make_output(image):
    cv.imwrite('outputof_'+input_image_old_name+'_'+input_image_new_name+'.png',image)

if __name__ == "__main__":

    binary_image_old = make_binary(input_image_old,"old")
    binary_image_new = make_binary(input_image_new,"new")
    top_contours_input_image_old = top_contours(binary_image_old)
    top_contours_input_image_new = top_contours(binary_image_new)
    output_image = read_image(input_image_new)
    draw_contours_red(top_contours_input_image_old,output_image)
    draw_contours_blue(top_contours_input_image_new,output_image)
    make_output(output_image)
   