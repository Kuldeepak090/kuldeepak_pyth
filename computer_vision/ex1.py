import cv2

img = cv2.imread("C:/Users\KULDEEPAK/Desktop/og-default-image.jpeg")
print("the image has", img.size,"pixels")
cv2.imshow("og-default-image",img)
cv2.imshow("og-default-image",img*2)
cv2.imshow("og-default-image",img/2)
cv2.imshow("og-default-image",img**12)
cv2.waitKey(0)
