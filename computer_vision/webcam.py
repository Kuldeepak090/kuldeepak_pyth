import cv2
from cv2 import VideoCapture

cap = VideoCapture(0)

while True:
    status,frame = cap.read()
    if not status:
        break
    cv2.imshow('window',frame)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()    