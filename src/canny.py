import cv2
import filters

def canny(img):
    img = filters.rgb2gray(img)
    img_smoothed = filters.convolve(img, filters.gaussian_kernel(5, 1))
    gradient_mat, theta_mat = filters.sobel_filters(img_smoothed)
    non_max_img = filters.non_max_suppression(gradient_mat, theta_mat)
    threshold_img = filters.threshold(non_max_img, weak_pixel=75, strong_pixel=255, low_threshold=0.05, high_threshold=0.15)
    img_final = filters.hysteresis(threshold_img, weak_pixel=75, strong_pixel=255)
    return img_final