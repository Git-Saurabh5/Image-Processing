import numpy as np
from PIL import Image
import math

image = np.array(Image.open("rotate.png"))   # Load the image
angle = int(input("Enter angle to rotate : "))

angle = math.radians(angle)
cosine  = math.cos(angle)
sine = math.sin(angle)
height = image.shape[0]
width = image.shape[1]

print(height,width)
new_height = round(abs(height*cosine) + abs(width*sine)) + 1
new_width = round(abs(width*cosine) + abs(height*sine)) + 1

output = np.zeros((new_height,new_width,image.shape[2]))

original_centre_ht =  round(((height+1)/2)-1)
original_centre_wd =  round(((width+1)/2)-1)

new_centre_ht =  round(((new_height+1)/2)-1)
new_centre_wd =  round(((new_width+1)/2)-1)

for i in range(height):
    for j in range(width):
        #co-ordinates of pixel with respect to the centre of original image
        y = height-1-i-original_centre_ht
        x = width-1-j-original_centre_wd
        
        #co-ordinate of pixel with respect to the rotated image
        new_y=round(-x*sine+y*cosine)
        new_x=round(x*cosine+y*sine)

        '''since image will be rotated the centre will change too, 
        so to adust to that we will need to change new_x and new_y with
        respect to the new centre'''
        new_y=new_centre_ht-new_y
        new_x=new_centre_wd-new_x
        
        # adding if check to prevent any errors in the processing
        if 0 <= new_x < new_width and 0 <= new_y < new_height and new_x>=0 and new_y>=0:
            output[new_y,new_x,:]=image[i,j,:]                          #writing the pixels to the new destination in the output image

pil_img=Image.fromarray((output).astype(np.uint8))    # converting array to image
pil_img.save("rotated_image.png")     