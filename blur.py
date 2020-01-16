import cv2
image=cv2.imread('assassin.jpg',1)
blur=cv2.blur(image,(5,5))
h=cv2.GaussianBlur(image,(5,5),0)
cv2.imshow('image',image)
cv2.imshow('blur',blur)
cv2.imshow('h',h)
cv2.waitKey(10000)
cv2.destroyAllWindows()