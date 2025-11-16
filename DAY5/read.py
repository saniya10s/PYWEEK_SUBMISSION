import cv2
import mediapipe as mp
import numpy as np
#Image Reading
import cv2
img=cv2.imread("Photos/cat.webp")
cv2.imshow("Cat",img)
cv2.waitKey(200)
cv2.destroyAllWindows()

#GrayScale Image
img=cv2.imread("Pictures/cat1.webp")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale Cat",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Gaussian Blur
img=cv2.imread("Pictures/cat1.webp")
blur=cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("Blurred Cat",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()



#Video Reading
cap=cv2.VideoCapture("Videos/cat.mp4")
while True:
     success, img=cap.read()
     if not success:
         break
     cv2.imshow("Video", img)
     if cv2.waitKey(1) & 0xFF == ord('q'):
         break
cap.release()
cv2.destroyAllWindows()

#Webcam Reading
cap=cv2.VideoCapture(0)

while True:
     success, img=cap.read()
     cv2.flip(img, 1, img)  # Mirror the image
     if not success:
         break
     cv2.imshow("Webcam", img)
     if cv2.waitKey(1) & 0xFF == ord('q'):
         break
cap.release()
cv2.destroyAllWindows()

#Video Reszing
 cap=cv2.VideoCapture(0)
 while True:
     success, img=cap.read()
     cv2.flip(img, 1, img)  # Mirror the image
     if not success:
         break

     img = cv2.resize(img, (640, 480)) 
     cv2.imshow("Resized Webcam", img)
     if cv2.waitKey(1) & 0xFF == ord('q'):
         break
 cap.release()
 cv2.destroyAllWindows()


