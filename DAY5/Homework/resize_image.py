import cv2

img = cv2.imread("input.jpg")

h, w = img.shape[:2]
new_w = w // 4
new_h = h // 4

resized_img = cv2.resize(img, (new_w, new_h))

cv2.imshow("Original", img)
cv2.imshow("Resized (1/4)", resized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()