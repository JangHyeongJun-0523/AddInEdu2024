import cv2
import numpy as np
img = cv2.imread("../data/candies.png")
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
def nothing(x):
    pass
cv2.namedWindow("HSV_Image")
cv2.createTrackbar('Low Hue Min', 'HSV_Image', 0, 179, nothing)
cv2.createTrackbar('Low Hue Max', 'HSV_Image', 0, 179, nothing)
cv2.createTrackbar('High Hue Min', 'HSV_Image', 0, 179, nothing)
cv2.createTrackbar('High Hue Max', 'HSV_Image', 0, 179, nothing)
cv2.createTrackbar('Sat Min', 'HSV_Image', 0, 255, nothing)
cv2.createTrackbar('Sat Max', 'HSV_Image', 0, 255, nothing)
cv2.createTrackbar('Val Min', 'HSV_Image', 0, 255, nothing)
cv2.createTrackbar('Val Max', 'HSV_Image', 0, 255, nothing)
while True:
    low_h_min = cv2.getTrackbarPos('Low Hue Min', 'HSV_Image')
    low_h_max = cv2.getTrackbarPos('Low Hue Max', 'HSV_Image')
    high_h_min = cv2.getTrackbarPos('High Hue Min', 'HSV_Image')
    high_h_max = cv2.getTrackbarPos('High Hue Max', 'HSV_Image')
    s_min = cv2.getTrackbarPos('Sat Min', 'HSV_Image')
    s_max = cv2.getTrackbarPos('Sat Max', 'HSV_Image')
    v_min = cv2.getTrackbarPos('Val Min', 'HSV_Image')
    v_max = cv2.getTrackbarPos('Val Max', 'HSV_Image')
    lower_color1 = np.array([low_h_min, s_min, v_min])
    upper_color1 = np.array([low_h_max, s_max, v_max])
    lower_color2 = np.array([high_h_min, s_min, v_min])
    upper_color2 = np.array([high_h_max, s_max, v_max])
    mask1 = cv2.inRange(hsv_img, lower_color1, upper_color1)
    mask2 = cv2.inRange(hsv_img, lower_color2, upper_color2)
    mask = cv2.bitwise_or(mask1, mask2)
    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("img", img)
    cv2.imshow("mask1", mask1)
    cv2.imshow("mask2", mask2)
    cv2.imshow("mask", mask)
    cv2.imshow('result', result)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()







