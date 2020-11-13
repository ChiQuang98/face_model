import cv2


img = cv2.imread("data_model/image.png")
height, width, channels = img.shape

subHeight = int(height/2)
subWidth = int(width/2)


cut_img = img[0:subHeight,0:subWidth]

resize_img = cv2.resize(img, (subWidth, subHeight), 3)

blur = cv2.GaussianBlur(img, (5, 5), 0)

edges = cv2.Canny(img, 100, 200)


