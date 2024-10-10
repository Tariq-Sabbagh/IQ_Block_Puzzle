import cv2
import numpy as np

from IQ_Block_Puzzle import get_bigcontour

import GetPieces

indexPices=[]
def getBoard(board,parts):
    j=0
    s=0
    valid=False
    global indexPices
    for index, part in enumerate(parts):
        for i, (lower, upper) in enumerate(color_ranges):
            hsv_image = cv2.cvtColor(part, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv_image, lower, upper)
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if contours:
                for contour in contours:
                    area=cv2.contourArea(contour)
                    if (area > 1000):
                        if i+1 not in indexPices:
                            indexPices.append(i+1)
                        board[s][j]=i+1
                        # print(area)
                        # color_num.append(i + 1)
                        # cnt=cnt+1
                        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
                        cv2.drawContours(part, [approx], -1, (0, 255, 0), 2)
                        # cv2.drawContours(resize_image, [approx], -1, (0, 255, 0), 2)
        j=j+1
        if j%8==0:
            s=s+1
            j=0
    # for row in board:
    #     print(row ,"\n")
    p = GetPieces.get_piece(indexPices)
    return board ,p

    # for index, part in enumerate(get_bigcontour.parts):
    #     part=cv2.resize(part,(500,500))
    #     cv2.imshow(f'Part {index + 1}', part)




# def printContour():
#
# contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#
# if contours:
#     for contour in contours:
#         area=cv2.contourArea(contour)
#         if (area > 1000):
#             # print(area)
#             color_num.append(i + 1)
#             cnt=cnt+1
#             approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
#             cv2.drawContours(resize_image, [approx], -1, (0, 255, 0), 2)
#             x , y ,w,h=cv2.boundingRect(approx)
#             print(x, ' ', y, ' ', w, ' ', h, '\n')

def showimage(parts):
    box_height, box_width = parts[0].shape[:2]
    combined_image = np.zeros((box_height * 8, box_width * 8, 3), dtype=np.uint8)

    for i in range(8):
        for j in range(8):
            index = i * 8 + j
            combined_image[i * box_height:(i + 1) * box_height,
            j * box_width:(j + 1) * box_width] = parts[index]

    # عرض الصورة المدمجة
    cv2.imshow('Combined Image', combined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def run_getBoard():
    image ,parts = get_bigcontour.run_code()
    resize_image=cv2.resize(image,(600,500))

    # hsv_image = cv2.cvtColor(resize_image, cv2.COLOR_BGR2HSV)



    board = [[0, 0, 0, 0, 0, 0, 0, 0] for _ in range(8)]
    board,pices= getBoard(board,parts)
    return board,pices
    # showimage(parts)

    # for i, (lower, upper) in enumerate(color_ranges):
    #     hsv_image = cv2.cvtColor(parts[0], cv2.COLOR_BGR2HSV)
    #     mask = cv2.inRange(hsv_image, lower, upper)
    #     getBoard(parts)






    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

color_ranges = [
        (np.array([0, 139, 189]), np.array([7, 191, 255])),   # piece 1
        (np.array([84, 128, 128]), np.array([99, 219, 246])),  # piece 2
        (np.array([89, 0, 95]), np.array([152, 95, 156])),  # piece 3
        (np.array([166, 134, 0]), np.array([179, 191, 168])),  # piece 4
        (np.array([0, 0, 0]), np.array([113, 109, 54])), # piece 5
        (np.array([46, 64, 149]), np.array([97, 137, 253])),# piece 6
        (np.array([6, 144, 106]), np.array([11, 229, 167])),# piece 7
        (np.array([0, 232, 177]), np.array([15, 255, 255])),# piece 8
        (np.array([18, 205, 172]), np.array([26, 255, 255])),# piece 9
        (np.array([77, 144, 68]), np.array([91, 255, 127])),# piece 10
        (np.array([99, 205, 73]), np.array([179, 255, 141])),# piece 11
        (np.array([24, 114, 160]), np.array([34, 255, 255])) # piece 12
    ]
