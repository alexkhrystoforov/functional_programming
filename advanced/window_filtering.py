import cv2
import threading
import numpy as np


img = cv2.imread('road.jpg')

h,w,c = img.shape
num_processes = 2

tile_size = int(h/num_processes)

tile_1 = img[:tile_size, :,:]
tile_2 = img[tile_size:h, :,:]

tiles = [tile_1, tile_2]
filtered_img = np.array([])


def blur_filter(tile):
    global filtered_img
    tile = cv2.medianBlur(tile, 7)
    filtered_img = np.append(filtered_img, tile)


for tile in tiles:
    t = threading.Thread(target=blur_filter, args=[tile])
    t.start()
    t.join()


filtered_img = filtered_img.reshape(h, w, c)
cv2.imwrite('filtered_img.png', filtered_img)

filtered_img = cv2.imread('filtered_img.png')
cv2.imshow('img', filtered_img)
cv2.waitKey(0)