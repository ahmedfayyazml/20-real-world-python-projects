import os #you dont have to put these
from curses.textpad import rectangle

os.environ["QT_QPA_PLATFORM"] = "xcb" #you dont have to put these
import time
import  cv2
from emailing import send_email

video = cv2.VideoCapture(0) # 0 of you are using your computer or laptop camera and 1 or 2 if external
time.sleep(1) ## it will negate the black color in the starting and help the camera load
first_frame = None
status_list = []
count = 0
while True:
    status = 0
    check,frame = video.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #convert the frame color into grey because it is less heavy
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21),0)  # applying gaussian blur to make calculations more efficient


    if first_frame is None:
        first_frame = gray_frame_gau

    delta_frame = cv2.absdiff(first_frame,gray_frame_gau) # absoulte difference between two frames

    thresh_frame = cv2.threshold(delta_frame,60,255,cv2.THRESH_BINARY)[1]

    dil_frame = cv2.dilate(thresh_frame,None,iterations=2)
    cv2.imshow("My Video", dil_frame)

    contours,check = cv2.findContours(dil_frame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour)<4000:
            continue
        x,y,w,h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)  ## wrap the object with a rectangle
        if rectangle.any():
            status = 1

    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[0]==1  and  status_list[1]==0:
        send_email()
    cv2.imshow("Video",frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
video.release()





