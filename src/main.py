from hough import hough_circles
from analyzer import analyze
from pathlib import Path
from contextlib import redirect_stdout
import cv2
import numpy as np
import canny

source_image = "images/coins.png"
result_path = "result/coins"

def hough_processed(source_image, canny_image):
    result_image = source_image.copy()
    circles = [(0, 0, 0)]
    hough_circles(canny_image, circles)

    for node in circles:
        cv2.circle(result_image, (node[1], node[0]), node[2], (255, 0, 0), 1)
    
    return result_image, circles

if __name__ == "__main__":    
    Path("./result").mkdir(parents=True, exist_ok=True)
    source_image = cv2.imread(source_image, 1)
    canny_image = canny.canny(source_image)
    cv2.imwrite(result_path + "_canny.png", np.uint8(canny_image))
    hough_image, circles = hough_processed(source_image, canny_image)
    cv2.imwrite(result_path + "_hough.png", np.uint8(hough_image))
    with open('./result/analyze_result.txt', 'w') as f:
        with redirect_stdout(f):
            analyze(circles[1:], hough_image)