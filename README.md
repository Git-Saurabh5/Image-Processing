# Image-Processing
This project is done under SRA assignments, Image Processing Tasks.

### Task1 : Image Rotation

The image can be rotated by any angle.It involves finding the centre of the Matrix and Shifting along the centre using Rotation Matrix.There are two methods of rotating the image following above approach
1. [Using Rotation Matrix](https://legacy.voteview.com/images/homework_1_1_18_2011.jpg)
2. [Using Shearing Rotation](https://sra-vjti.github.io/2020/09/09/sheer-transformation.html)



|<img src="https://github.com/Git-Saurabh5/Image-Processing/blob/master/Image_Rotation/rotate.png">| 
|:---:|
|Input Image|

**Output**
### For Input angle 45°
|<img src="https://github.com/Git-Saurabh5/Image-Processing/blob/master/Image_Rotation/rotated_image.png">|<img width="640" height="450" src="https://github.com/Git-Saurabh5/Image-Processing/blob/master/Image_Rotation/rotated_image_using_shear.png">|
|:---:|:---:|
|Rotation Matrix|Shearing Rotation Matrix|

### 2. Applying Kernels

Convolution is a simple mathematical operation which is fundamental to many common image processing operators. Convolution provides a way of multiplying together two arrays of numbers, generally of different sizes, but of the same dimensionality, to produce a third array of numbers of the same dimensionality.Kernels form the Second Matrix which provides effects to the Image.
![figure3](https://user-images.githubusercontent.com/35737777/68632479-95c61f80-04e6-11ea-80b2-2e86a4fcc258.jpg)

* Applying 3X3, 5X5 filters to do the following task:
  * Blurring 
  * Sharpening

|<img src="https://github.com/Git-Saurabh5/Image-Processing/blob/master/Kernels/test_blur.png">|
|:---:|
|Input Image|

**Output**
|<img src="https://github.com/Git-Saurabh5/Image-Processing/blob/master/Kernels/blurred_image.png">|<img src="https://github.com/Git-Saurabh5/Image-Processing/blob/master/Kernels/gaussian_image.png">|<img src="https://github.com/Git-Saurabh5/Image-Processing/blob/master/Kernels/sharpen_image.png">|
|:---:|:---:|:---:|
|Box Blur|Gaussian Blur|Sharpen|




