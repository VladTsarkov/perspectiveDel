import cv2
import numpy as np
img = cv2.imread('test.jpg')
src = np.array([
[497,124],
[693,19],
[742,588],
[464,563]], dtype = "float32")
(tl,tr,br,bl)=src
widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
maxWidth = max(int(widthA), int(widthB))
heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
maxHeight = max(int(heightA), int(heightB))
dst = np.array([
[0, 0],
[maxWidth - 1, 0],
[maxWidth - 1, maxHeight - 1],
[0, maxHeight - 1]], dtype = "float32")
M = cv2.getPerspectiveTransform(src, dst)
warped = cv2.warpPerspective(img, M, (maxWidth, maxHeight))
cv2.imwrite('test_1.jpg',warped)
