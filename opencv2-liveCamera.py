import cv2

cap = cv2.VideoCapture(-1)

if cap.isOpened() == False:
    print("Can't Open Camera")
    cv2.destroyAllWindows()

while(True):
    ret, img_frame = cap.read()
    if ret == False:
        print("Fail to Capture")
        break;

    cv2.imshow('Color', img_frame)
    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
