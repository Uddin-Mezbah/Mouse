import cv2
import numpy as np
from math import sqrt

def calc_distance(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return round(sqrt((x1-x2)**2 + (y1-y2)**2))

# param contains the center and the color of the circle 
def draw_red_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        center = (x,y)#param[0]
        radius = 2#calc_distance((x, y), center)
        cv2.circle(img, center, radius, center, 2)


img = np.zeros((512,512,3), np.uint8)

# create a windows
cv2.namedWindow("img_red")

param = [(200,200),(0,0,255)]
cv2.setMouseCallback("img_red", draw_red_circle, param)


while True:
    # both windows are displaying the same img
    cv2.imshow("img_red", img)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()