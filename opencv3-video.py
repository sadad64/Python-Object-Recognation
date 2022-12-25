import cv2

cap = cv2.VideoCapture(-1)

if cap.isOpened() == False:
    print("Can't Open Camera")
    cv2.destroyAllWindows()

ret, img_frame = cap.read()

if ret == False:
    print("Fail to Capture")
    exit(1)

codec = cv2.VideoWriter_fourcc('M','J','P','G')
fps = 10.0
h,w = img_frame.shape[:2]
writer = cv2.VideoWriter('/home/pi/onuput.avi', codec, fps, (w,h))

if writer.isOpened() == False:
    print("Can't ready the video file")
    exit(1)

while(True):
    ret, img_frame = cap.read()

    if ret == False:
        print("Capture Failed")
        break

    writer.write(img_frame)

    cv2.imshow('Color', img_frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
