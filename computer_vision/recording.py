import cv2
from cv2 import VideoCapture
from cv2 import VideoWriter

cap = VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 60.0, (640,  480))

while True:
    status,frame = cap.read()
    if not status:
        break
    cv2.imshow('window',frame)
    out.write(frame)
    if cv2.waitKey(1) == 27:
        break
out.release()
cap.release()
cv2.destroyAllWindows()  