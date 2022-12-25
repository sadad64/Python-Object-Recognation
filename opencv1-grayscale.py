import cv2

image = '/home/pi/test.jpg'
gray_img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

cv2.imshow('result', gray_img)

k = cv2.waitKey(0)&0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('/home/pi/gray_test.jpg', gray_img)
    cv2.destroyAllWindows()