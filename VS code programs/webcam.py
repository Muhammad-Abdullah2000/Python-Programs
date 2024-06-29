import cv2
from cv2 import CAP_ANDROID
url = "192.168.1.177"
cp = cv2.VideoCapture(url)
while(True):
    camera, frame = CAP_ANDROID.read()
    if frame is not None:
        cv2.imshow("Frame", frame)
    q = cv2.waitKey(1)
    if q==ord("q"):
        break
cv2.destroyAllWindows()