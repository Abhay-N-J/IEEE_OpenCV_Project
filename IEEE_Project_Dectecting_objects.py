
import numpy as np
import cv2 as cv


#Change Address of the image
imageFrame = cv.imread('Trial.jpeg') 

global images 
images = []
  
# Start a while loop
# while(1):
    
# Reading the video from the
# webcam in image frames
# _, imageFrame = webcam.read()

# Convert the imageFrame in 
# BGR(RGB color space) to 
# HSV(hue-saturation-value)
# color space
hsvFrame = cv.cvtColor(imageFrame, cv.COLOR_BGR2HSV)

# Set range for red color and 
# define mask
red_lower = np.array([0, 50, 50], np.uint8)
red_upper = np.array([10, 255, 255], np.uint8)
red_mask = cv.inRange(hsvFrame, red_lower, red_upper)

# Set range for green color and 
# define mask
green_lower = np.array([50, 100, 100], np.uint8)
green_upper = np.array([60, 255, 255], np.uint8)
green_mask = cv.inRange(hsvFrame, green_lower, green_upper)

# Set range for blue color and
# define mask
blue_lower = np.array([94, 80, 2], np.uint8)
blue_upper = np.array([120, 255, 255], np.uint8)
blue_mask = cv.inRange(hsvFrame, blue_lower, blue_upper)

# Set range for orange color and
# define mask
orange_lower = np.array([10,100,20],np.uint8)
orange_upper = np.array([25,255,255],np.uint8)
orange_mask = cv.inRange(hsvFrame, orange_lower,orange_upper)

# Set range for yellow color and
# define mask
yellow_lower = np.array([25,255,255], np.uint8)
yellow_upper = np.array([45,255,255], np.uint8)
yellow_mask = cv.inRange(hsvFrame, yellow_lower, yellow_upper)


# Morphological Transform, Dilation
# for each color and bitwise_and operator
# between imageFrame and mask determines
# to detect only that particular color
kernal = np.ones((5, 5), "uint8")
    
# For red color
red_mask = cv.dilate(red_mask, kernal)
# res_red = cv.bitwise_and(imageFrame, imageFrame, 
                            # mask = red_mask)
    
# For green color
green_mask = cv.dilate(green_mask, kernal)
# res_green = cv.bitwise_and(imageFrame, imageFrame,
                            # mask = green_mask)
    
# For blue color
blue_mask = cv.dilate(blue_mask, kernal)
# res_blue = cv.bitwise_and(imageFrame, imageFrame,
                            # mask = blue_mask)

# For orange color
orange_mask = cv.dilate(orange_mask,kernal)
# res_orange = cv.bitwise_and(imageFrame, imageFrame,
                            #  mask = orange_mask)

# For Yellow color
yellow_mask = cv.dilate(yellow_mask, kernal)
# res_yellow = cv.bitwise_and(imageFrame, imageFrame,
                            # mask = yellow_mask)

def shape_creater(contour,imageFrame,color,l):
    
        
    shape = cv.approxPolyDP(
        contour, 0.01 * cv.arcLength(contour, True), True)
    # cv.drawContours(imageFrame,[contour],0,color,2)
        # finding center point of shape
    M = cv.moments(contour)
    if M['m00'] != 0.0:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])
        
  
    # putting shape name at center of each shape
    if len(shape) == 3:
        cv.putText(imageFrame, 'Triangle', (x, y),
                    cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 2)
        l.append('Triangle')
        
  
    elif len(shape) == 4 & x==y:
        cv.putText(imageFrame, 'Square', (x, y),
                    cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 2)
        l.append('Sqaure')
    elif len(shape) == 4:
        cv.putText(imageFrame, 'Rectangle', (x, y),
                    cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 2)
        l.append('Rectangle')
    elif len(shape) == 5:
        cv.putText(imageFrame, 'Pentagon', (x, y),
                    cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 2)
        l.append('Pentagon')
  
    elif len(shape) == 6:
        cv.putText(imageFrame, 'Hexagon', (x, y),
                    cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 2)
        l.append('Hexagon')
  
    elif len(shape) == 7:
        cv.putText(imageFrame, 'Heptagon', (x, y),
                    cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 2)
        l.append('Heptagon')
    
    else:
        cv.putText(imageFrame, 'circle', (x, y),
                    cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 2)
        l.append('Circle')
    if M['m00'] != 0.0:
        l.append((x,y))
    return l


    
# Creating contour to track red color
contours, hierarchy = cv.findContours(red_mask,
                                        cv.RETR_TREE,
                                        cv.CHAIN_APPROX_SIMPLE)

for pic, contour in enumerate(contours):
    area = cv.contourArea(contour)
    
    x, y, w, h = cv.boundingRect(contour)
    # imageFrame = cv.rectangle(imageFrame, (x, y), 
    #                             (x + w, y + h), 
    #                             (0, 0, 255), 2)
    l = []
    l.append('RED')
    cv.putText(imageFrame, "Red Colour", (x, y),
                cv.FONT_HERSHEY_SIMPLEX, 0.6,
                (0, 0, 255))  
    r = shape_creater(contour,imageFrame,(0,0,255),l)
    images.append(r)
# Creating contour to track green color
contours, hierarchy = cv.findContours(green_mask,
                                        cv.RETR_TREE,
                                        cv.CHAIN_APPROX_SIMPLE)
    
for pic, contour in enumerate(contours):
    area = cv.contourArea(contour)
    
    x, y, w, h = cv.boundingRect(contour)
    # imageFrame = cv.rectangle(imageFrame, (x, y), 
    #                             (x + w, y + h),
    #                             (0, 255, 0), 2)
    l = []
    l.append('Green')
        
    cv.putText(imageFrame, "Green Colour", (x, y),
                cv.FONT_HERSHEY_SIMPLEX, 
                0.6, (0, 255, 0))
    r = shape_creater(contour,imageFrame,(0,255,0),l)
    images.append(r)
        

# Creating contour to track blue color
contours, hierarchy = cv.findContours(blue_mask,
                                        cv.RETR_TREE,
                                        cv.CHAIN_APPROX_SIMPLE)
for pic, contour in enumerate(contours):
    area = cv.contourArea(contour)
    
    x, y, w, h = cv.boundingRect(contour)
    # imageFrame = cv.rectangle(imageFrame, (x, y),
    #                             (x + w, y + h),
    #                             (255, 0, 0), 2)
    l = []
    l.append('Blue')
    cv.putText(imageFrame, "Blue Colour", (x, y),
                cv.FONT_HERSHEY_SIMPLEX,
                0.6, (255, 0, 0))
    r = shape_creater(contour,imageFrame,(255,0,0),l)
    images.append(r)    
# Creating contour to track orange color
contours, hierarchy = cv.findContours(orange_mask,
                                        cv.RETR_TREE,
                                        cv.CHAIN_APPROX_SIMPLE)
for pic,contour in enumerate(contours):
    area = cv.contourArea(contour)
    
    x,y,w,h = cv.boundingRect(contour)
    # imageFrame = cv.rectangle(imageFrame, (x,y), 
    #                             (x+w,y+h),
    #                             (10,200,255),2)
    l = []
    l.append('Orange')
    cv.putText(imageFrame,"Orange Colour", (x,y),
                cv.FONT_HERSHEY_SIMPLEX,
                0.6 ,(10,200,255))     
    r = shape_creater(contour,imageFrame,(10,255,255),l)
    images.append(r)
# Creating contour to track yellow color
contours, hierarchy = cv.findContours(yellow_mask,
                                        cv.RETR_TREE,
                                        cv.CHAIN_APPROX_SIMPLE)
for pic,contour in enumerate(contours):
    area = cv.contourArea(contour)
    
    x,y,w,h = cv.boundingRect(contour)
    # imageFrame = cv.rectangle(imageFrame, (x,y), 
    #                             (x+w,y+h),
    #                             (0,255,255),2)
    l = []
    l.append('Yellow')
    cv.putText(imageFrame,"Yellow Colour", (x,y),
                cv.FONT_HERSHEY_SIMPLEX,
                0.6 ,(0,255,255))   
    r = shape_creater(contour,imageFrame,(0,255,255),l)
    images.append(r)
         


print(images)

# Program Termination
cv.imshow("Multiple Color Detection in Real-TIme", imageFrame)

if cv.waitKey() & 0xFF == ord('q'):
    # webcam.release()
    cv.destroyAllWindows()
    