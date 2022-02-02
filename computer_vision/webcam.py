from cv2 import VideoCapture
import numpy as np
from cv2 import VideoCapture

cap = VideoCapture(0)

while True:
    status,frame = cap.read()
    if not status:
        print (status)
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow('window',frame)
    cv2.imshow('gray',gray)
    merged = np.hstack(frame,rgb)
    cv2.imshow("merged",merged)
    if cv2.waitkey(1) == 27:
        break

cap.realse()
cv2.destroyAllWindoes()    