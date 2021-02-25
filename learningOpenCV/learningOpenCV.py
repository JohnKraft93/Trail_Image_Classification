import imutils 
import cv2
import numpy as np
import matplotlib.pyplot as plt #importing matplotlib

#Reading the image
image = cv2.imread('road.jpg')

h, w = image.shape[:2]

print("Height = {}, Width = {}".format(h,w))

'''display image'''
#cv2.imshow("title", image)

# waits to proceed until image window is closed
#cv2.waitKey(0)
#cv2.destroyAllWindows()

'''opens image in greyscale'''
#greyscale_image = cv2.imread('road.jpg', 0)
#cv2.imshow("title", greyscale_image)

'''saving new photo'''
#cv2.imwrite("greyscaleRoad.jpg", greyscale_image)


'''Displaying only specific colors'''

#skier = cv2.imread('skiier.jpeg')

#cv2.imshow("Skier", skier)

#img = cv2.imread('bgr_img.png')
#B, G, R = cv2.split(img)

#cv2.imshow("blue", B)
#cv2.imshow("green", G)
#cv2.imshow("red", B)


'''adding two images together'''

#image1 = cv2.imread('road.jpg')
#image2 = cv2.imread('marc.jpg')
#image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
#weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
#cv2.imshow('weighted images',   weightedSum)


'''subtracting two images'''

#sub = cv2.subtract(image1, image2)
#cv2.imshow("subtracting two images", sub)


'''Bitwise Operations on Binary images'''

#image1 = cv2.imread('bitwise_img1.png')
#image2 = cv2.imread('bitwise_img2.png')

#andImg = cv2.bitwise_and(image1, image2, mask = None)
#orImg = cv2.bitwise_or(image1, image2, mask = None)
#xorImg = cv2.bitwise_xor(image1, image2, mask = None)
#notImg = cv2.bitwise_not(image1, mask = None) #inverse of image

#cv2.imshow("AND", andImg)
#cv2.imshow("OR", orImg)
#cv2.imshow("xor", xorImg)


'''Eroding an image'''

#image = cv2.imread("road.jpg", 1)

#kernel = np.ones((6,6), np.uint8)

#image = cv2.erode(image, kernel)
#cv2.imshow("eroded image", image)


'''Gaussian Blur'''

#Gaussian = cv2.GaussianBlur(image, (17, 17), 0) 
#cv2.imshow('Gaussian Blurring', Gaussian) 
#cv2.waitKey(0)


'''scaling image'''

#new_img = cv2.resize(image, (int(w/2), int(h/2)), interpolation=cv2.INTER_CUBIC)
#cv2.imshow("scale", new_img)


'''rotating image with respect to the center'''

#M = cv2.getRotationMatrix2D((w / 2, h / 2), 45, 1) 
#ret = cv2.warpAffine(image, M, (w, h)) 
#cv2.imshow('rotate', res)


'''shifting an image'''

#M = np.float32([[1, 0, -200], [0, 1, 250]]) 
#ret = cv2.warpAffine(image, M, (w, h)) 
#cv2.imshow('shift', ret)


'''edge detection'''

#edgeimg = cv2.Canny(image, 100, 200)
# cv2.imshow('edge1', edgeimg)

# edgeimg = cv2.Canny(image, 1000, 2000)
# cv2.imshow('edge2', edgeimg)

# edgeimg = cv2.Canny(image, 10, 20)
# cv2.imshow('edge3', edgeimg)

# edgeimg = cv2.Canny(image, 200, 300)
# cv2.imshow('edge4', edgeimg)

# edgeimg = cv2.Canny(image, 75, 150)
# cv2.imshow('edge5', edgeimg)


'''Erosion and dilation'''

# kernel = np.ones((5,5), np.uint8) 

# er = cv2.erode(image, kernel, iterations=1)
# di = cv2.dilate(image, kernel, iterations=1)
     
# cv2.imshow("erosion", er)
# cv2.imshow("dilation", di)


#testing different kernels

# kernel = np.ones((7,7), np.uint8) 

# er = cv2.erode(image, kernel, iterations=1)
# di = cv2.dilate(image, kernel, iterations=1)
     
# cv2.imshow("erosion", er)
# cv2.imshow("dilation", di)



peopleimg = cv2.imread('img_w_snowmobiler.jpg', 0)
cv2.imshow("og", peopleimg)
peopleimgCol = cv2.imread('img_w_snowmobiler.jpg')
clrimg = cv2.imread('clearimg.jpg', 0)
#cv2.imshow('people', peopleimg)

'''using histogram with plt if there are a lot of darker colors in the image'''
'''Could be valuable in decidding if there are 0 people in the image vs multiple

people = plt.figure(1)
plt.hist(peopleimg.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k') #calculating histogram
people.show()

clr = plt.figure(2)
plt.hist(clrimg.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k') #calculating histogram
clr.show()

# There's a clear different an image with no one in it and the one with it
# Trying to find an with no one in it to base off other image off of could be 
# difficult to do without doing it manually


histogram equalization'''

ret = cv2.equalizeHist(peopleimg)
ret2 = np.hstack((peopleimg, ret))
cv2.imshow('stacked', ret2)

# makes darker items in image darker blobs
# could be beneficial to identify number of blobs?


'''thresholding: creating blobs?'''
#adjust thresholdVal(ex. 120) to vary what gets coverted to a 0 and what one get converted to a 1

#ret, threshold = cv2.threshold(peopleimg, 120, 255, cv2.THRESH_BINARY) 
#cv2.imshow('Binary Threshold', threshold)

#threshold2 = cv2.adaptiveThreshold(peopleimg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 199, 30) 
#cv2.imshow('threshold', threshold2)

# I tested other threshold techniques but cv2.THRESH_BINARY seemed to be good but  
# adaptive seemed to be the best 


'''denoise the color'''

#ret = cv2.fastNlMeansDenoisingColored(peopleimgCol, None, 10, 10, 7, 15) 
#ret2 = np.hstack((peopleimgCol, ret))
#cv2.imshow('denoise', ret2)

#Can be beneficial to remove sharp colors such as tree edges or snowflake if it is dumping snow



'''THROW AWAY PROGRAM THAT COUNTS THE NUMBER OF DOTS WITHIN AN IMAGE
SIMILAR TO COUNTING THE OF PEOPLE WITHIN A PHOTO (0, 1, 2+)
'''
dotimg = cv2.imread('black-dot1.jpg', 0)
h, w = dotimg.shape[:2]
dotimg = cv2.resize(dotimg, (int(w*4), int(h*4)), interpolation=cv2.INTER_CUBIC)
cv2.imshow("dotimg", dotimg)

threshold = cv2.adaptiveThreshold(dotimg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 199, 30) 

cv2.imshow("new", threshold)

cnts = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2] 

s1 = 3*4*4
s2 = 20*4*4
xcnts = [] 
for cnt in cnts: 
    print(cv2.contourArea(cnt))
    if s1 < cv2.contourArea(cnt) < s2: 
        xcnts.append(cnt) 

print("dots: ", str(len(xcnts)))

#BE CAREFUL WITH resize and contour areas. On this testing program, I scaled the image by 4
# then i needed to scale the areas by 4^2. 
'''

Future testing:
Test relationship between resizeing and contour areas on more images.
Look more into contour areas and how they work.

is there a step by step process that will be best to classify images into the number of people
in the image. Ex. First, seperate them using histograms. Then, see how edge detection can be
used to seperate images. Finally, use thresholds and contour areas to say how many people/living
things are in the image
'''


'''
With our first step being to seperate the images into useful images and unuseful
images, I believe OpenCV is our best bet to get an accurate sub dataset with only
important images.
'''







