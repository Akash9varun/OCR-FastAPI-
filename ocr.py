import cv2
import pytesseract 

img = cv2.imread('7.png')
cv2.imshow('sample image' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()

text = pytesseract.image_to_string(img)
print(text)