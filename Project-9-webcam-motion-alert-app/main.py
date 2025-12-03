import os #you dont have to put these
os.environ["QT_QPA_PLATFORM"] = "xcb" #you dont have to put these
import time
import  cv2

video = cv2.VideoCapture(0) # 0 of you are using your computer or laptop camera and 1 if external
time.sleep(1) ## it will negate the black color in the starting and help the camera load

while True:
    check,frame = video.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #convert the frame color into grey because it is less heavy
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21),0)  # applying gaussian blur to make calculations more efficient
    cv2.imshow("My Video", gray_frame_gau)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
video.release()





