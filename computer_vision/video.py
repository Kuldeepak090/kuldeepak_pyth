import cv2

cap = cv2.VideoCapture("F:/Defance exfo/VID_20200207_120101.mp4")

while True:
    status, frame = cap.read()
    h,w,_ = frame.shape
    if not status:
        print("status is missing")
        break
    frame_sm = cv2.resize(frame,(w//2,h//2))
    cv2.imshow("Output", frame)  
    if cv2.waitKey(1) =='27':
         break 

cap.realse()  
cv2.destroyAllWindows()






