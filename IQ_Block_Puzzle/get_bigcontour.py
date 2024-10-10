from time import sleep

import cv2
import numpy as np
import getPhoto

def preProcess(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # CONVERT IMAGE TO GRAY SCALE
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)  # ADD GAUSSIAN BLUR
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, 1, 1, 11, 2)  # APPLY ADAPTIVE THRESHOLD
    return imgThreshold


def reorder(myPoints):
    myPoints = myPoints.reshape((4, 2))
    myPointsNew = np.zeros((4, 1, 2), dtype=np.int32)
    add = myPoints.sum(1)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    return myPointsNew


#### 3 - FINDING THE BIGGEST COUNTOUR ASSUING THAT IS THE SUDUKO PUZZLE
def biggestContour(contours):
    biggest = np.array([])
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 50:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            if area > max_area and len(approx) == 4:
                biggest = approx
                max_area = area
    return biggest, max_area

# img =cv2.VideoCapture(0)
# while True:
#     _,frame=img.read()
#     cv2.imwrite("green.png",frame)
#     cv2.waitKey(0)
def run_code():
    img =cv2.imread('board.jpg')
    # img = getPhoto.takePhoto()
    img = cv2.resize(img, (460, 460))
    imgBlank = np.zeros((460, 460, 3), np.uint8)  # CREATE A BLANK IMAGE FOR TESTING DEBUGING IF REQUIRED
    imgThreshold = preProcess(img)

    imgContours = img.copy()  # COPY IMAGE FOR DISPLAY PURPOSES
    imgBigContour = img.copy()  # COPY IMAGE FOR DISPLAY PURPOSES
    contours, hierarchy = cv2.findContours(imgThreshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # FIND ALL CONTOURS
    cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 10)  # DRAW ALL DETECTED CONTOURS

    biggest, maxArea = biggestContour(contours)  # FIND THE BIGGEST CONTOUR

    # print(biggest)
    if biggest.size != 0:
        biggest = reorder(biggest)
        cv2.drawContours(imgBigContour, biggest, -1, (0, 0, 255), 25)  # DRAW THE BIGGEST CONTOUR
        pts1 = np.float32(biggest)  # PREPARE POINTS FOR WARP
        pts2 = np.float32([[0, 0], [460, 0], [0, 460], [460, 460]])  # PREPARE POINTS FOR WARP
        matrix = cv2.getPerspectiveTransform(pts1, pts2)  # GER
        imgWarpColored = cv2.warpPerspective(img, matrix, (460, 460))
        imgDetectedDigits = imgBlank.copy()
        # imgWarpColored = cv2.cvtColor(imgWarpColored,cv2.COLOR_BGR2BGRA)
        # boxes = splitImage(imgWarpColored, 8, 8)
        # عرض الأجزاء المقسم
        # for index, box in enumerate(boxes):
        #     cv2.imshow(f'Box {index + 1}', box)
        img_c = imgWarpColored.copy()
        img_c = img_c[25:425, 25:425]
        brightness =3
        # Adjusts the contrast by scaling the pixel values by 2.3
        contrast = 1.3
        img_c = cv2.addWeighted(img_c, contrast, np.zeros(img_c.shape, img_c.dtype), 0, brightness)
        parts=[]
        vertical_splits = np.vsplit(img_c, 8)
        for v_split in vertical_splits:
            horizontal_splits = np.hsplit(v_split, 8)
            parts.extend(horizontal_splits)
        # cv2.imshow('befor', img_c)
        # cv2.waitKey(0)

        # cv2.imshow('after', img_c)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        return img_c,parts
        # for index, part in enumerate(parts):
        #     part=cv2.resize(part,(500,500))
        #     cv2.imshow(f'Part {index + 1}', part)
        # combined_image = np.zeros((imgWarpColored.shape[0], imgWarpColored.shape[1], 3), dtype=np.uint8)



