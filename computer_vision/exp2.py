import cv2
cap = cv2.VideoCapture(0)

while True:
    status,img = cap.read()
    if status:
        fast = cv2.FastFeatureDetector_create()
        kp = fast.detect(img,None)
        img2 = cv2.drawKeypoints(img, kp, None, color=(0,255,255))
        cv2.imshow('window', img2)
        if cv2.waitKey(1) == 27:
            break
cap.release()
cv2.destroyAllWindows()
        