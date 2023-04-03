import cv2
import os
# 图片和当前程序在同一文件夹下，照片的命名方式为：1.jpg,2.jpg......100.jpg....1000.jpg...
fps = 25
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(filename='c.mp4', fourcc=fourcc, fps=fps, frameSize=(640, 480))  # 大小要和图片实际大小一样
num = 1000  # 照片的数量
for i in range(1, 1000):
    if os.path.exists(str(i) + '.jpg'):
        img = cv2.imread(filename=str(i) + '.jpg')
        cv2.waitKey(100)
        video_writer.write(img)
video_writer.release()
