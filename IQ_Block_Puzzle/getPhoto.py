import cv2
import time

def takePhoto():
    cap=cv2.VideoCapture(2)
    last_time=time.time()
    stop=2
    path= "board.jpg"
    while True:
        ret,frame=cap.read()
        # cv2.imshow("frame",frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
        if time.time()-last_time>=stop:
            cv2.imwrite(path,frame)
            return frame

cv2.destroyAllWindows()