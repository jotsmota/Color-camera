import cv2
import numpy as np
import time
import math

cam = cv2.VideoCapture(0)
cam.set(cv2.cv.CV_CAP_PROP_FPS,20)
cam2 = cv2.VideoCapture(1)
cam2.set(cv2.cv.CV_CAP_PROP_FPS,20)

cv2.namedWindow("camera1")
#cv2.namedWindow("camera2")
print("Processing ...")
time.sleep(3)
print("Start!")
print("Connecting to cameras")


img_counter = 0
na = 0

while True:
    ret,frame = cam.read()
    ret2,frame2 = cam2.read()
    # ret2,frame2 = cam2.read()
    # cv2.imshow("test",frame)
    a = math.floor(time.time())    
    while not ret and not ret2:
        print("...")
        ret,frame = cam.read()
        ret2,frame2 = cam2.read()
        if math.floor(time.time()) > a+15:
            break
    
    k = cv2.waitKey(1)
    

    if k%256 == 27:
        # ESC
        print("Escape hit, closing ...")
        break
 
    b = a%5
    
    if b == 0 and na != a:
        print("A: {}".format(a))
        mdn = np.mean(frame.astype(np.uint8))
        mdn2 = np.mean(frame2.astype(np.uint8))
        print("     Frame 1 mean color = {}".format(mdn))
        print("     Frame 2 mean color = {}".format(mdn2))
        cv2.imshow("camera1",frame)

    na = a

    
cam.release()
cam2.release()
cv2.waitKey(1)
cv2.destroyAllWindows()

