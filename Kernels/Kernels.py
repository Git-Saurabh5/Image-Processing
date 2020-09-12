
from PIL import Image
import numpy as np


def filter(image, kernel):
    new_image = np.zeros((image.shape[0]+kernel.shape[0]-1, image.shape[1]+kernel.shape[1]-1, image.shape[2]))
    new_image[kernel.shape[0]-2:-1:,kernel.shape[1]-2:-1:,:] = image
    new_image[0,0,:]=image[0,0,:]
    new_image[-1,-1,:]=image[-1,-1,:]
    output = np.zeros_like(image)
    for i in range(image.shape[1]):
        for j in range(image.shape[0]):
            for k in range(image.shape[2]):
                image_matrix = new_image[j : j+kernel.shape[1]  , i: i+kernel.shape[0], k]
                output[j, i, k] = np.sum(kernel * image_matrix)
    return output



gaussian_blurr=np.array([[1,  4,  6,  4, 1],
                         [4, 16, 24, 16, 4],
                         [6, 24, 36, 24, 6],
                         [4, 16, 24, 16, 4],
                         [1,  4,  6,  4, 1]])/256


                         
box_blur=np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]])/9
                  

sharpen_filter = np.array([[-1,-1,-1,-1,-1],
                            [-1,-1,-1,-1,-1],
                            [-1,-1,25,-1,-1],
                            [-1,-1,-1,-1,-1],
                            [-1,-1,-1,-1,-1]])/-25

image = Image.open('C:\\Users\\Admin\\Desktop\\Projects\\IP\\Kernels\\test_blur.png')
img = np.array(image)
boxblur_image = Image.fromarray(filter(img, box_blur))
boxblur_image.save("blurred_image.png")
gblur_image = Image.fromarray(filter(img, gaussian_blurr))
gblur_image.save("gaussian_image.png")
sharpen_image = Image.fromarray(filter(img, sharpen_filter))
sharpen_image.save("sharpen_image.png") 