import numpy as np
import cv2

#read in photo to scan use 0 to make these grey scale due to the alogothim used in cv2
img = cv2.imread('C:\\Users\\willr\\Documents\\GitHub\\OPENCV\\Learn\\waldo\\FindHard.jpg', 0)
#item to look for use 0 to make these grey scale due to the alogothim used in cv2
template = cv2.imread('C:\\Users\\willr\\Documents\\GitHub\\OPENCV\\Learn\\waldo\\WaldoForBeach.jpg', 0)

#gets the shape
h, w = template.shape


# testing 2d array 
# print(img)


# all the medthods for matching during testing will see which one works best
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
#after testing cv2.TM_CCORR wasnt the best
#methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]


for curr in methods:
    img2 = img.copy()
    
    #provides us with a convolution(takes our template and slides it across our img and tries to make it)
    result = cv2.matchTemplate(img2, template, curr)
    
    
    # gets the size needed to compare 
    # e.g. 
    # if the image is 4x4 and the template is 2x2 this will get the avg 3x3 and that will slide in 3x3 to get max coverage on the img
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # prints all the possible locations
    print(min_loc, max_loc)
    
    # using these methods cause they get the smallest size
    if(curr in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]):
        location = min_loc
    else:
        location = max_loc
        
    # putting a rectangle around the found item
    
    bottom_right = (location[0] + w, location[1] + h )
    cv2.rectangle(img2, location, bottom_right, (255, 23, 74), 10)
    cv2.imshow("Match", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()