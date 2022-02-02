from cv2 import VideoCapture
import numpy as np
from cv2 import VideoCapture

cap = VideoCapture(0)

fourcc =cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0(640,480))

while True:
    status,frame = cap.read()
    if not status:
        break
    
    cv2.imshow('window',frame)
    out.write(frame)
    if cv2.waitkey(1) == 27:
        break

out.realse()
cap.realse()
cv2.destroyAllWindoes()   