#importing the modules .
import cv2 
import numpy as np 

#Set width and height of the output stream.
frameWidth=800
frameHeight=480 

#capture the video from webcam .
cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,frameWidth)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,frameHeight)
#set brightness level.
BRIGHTNESS=150

def doNothing(x):
    pass

#Create window for the  webcam

cv2.namedWindow("WebCam",cv2.WINDOW_NORMAL)
#CreateTrackbar for regulating brightness.
cv2.createTrackbar("Change-Brightness","WebCam",BRIGHTNESS,300,doNothing)
myColors=[[5,107,0,19,255,255],
[133,56,0,159,156,255],
[57,76,0,100,255,255],
[90,48,0,118,255,255]]

#Colors used in painting .
myColorValues=[[51,153,255],
[255,0,255],
[0,255,0],
[255,0,0]]

myPoints=[]

#function to pick color of object .
def findColor(img,myColors,myColorValues):
     #Converting the image to hsv  format .
     imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
     count=0
     newPoints=[]

     for color in myColors:
         lower=np.array(color[0:3])
         upper=np.array(color[3:6])
         mask=cv2.inRange(imgHSV,lower,upper)
         x,y=getContours(mask)
         #making the circle 
         cv2.circle(imgResult,(x,y),15,myColorValues[count],cv2.FILLED)
         
         if x!= 0 and y!=0:
             newPoints.append([x,y,count])
             count+=1
     return newPoints


#get contours .
def getContours(img):
    contours,hierachy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    #Working with contours .
    for contour in contours:
        area=cv2.contourArea(contour)
        if area>500:
            peri=cv2.arcLength(contour,True)
            approx=cv2.approxPolyDP(contour,0.02*peri,True)
            x,y,w,h=cv2.boundingRect(approx)
    return  x+w//2,y 


def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult,(point[0],point[1]),10,myColorValues[point[2]],cv2.FILLED)





while True :
    succes,img=cap.read()
    imgResult=img.copy()
    #find the colors  for the points .
    newPoints=findColor(img,myColors,myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        #drawing the points .
        drawOnCanvas(myPoints,myColorValues)
    cv2.imshow("WebCam",imgResult)
    key=cv2.waitKey(1)
    if key==ord("q"):
        break


    











        


       
       


