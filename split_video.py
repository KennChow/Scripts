import os
import glob
import cv2

# 定义视频文件的扩展名
video_extensions = ['.mp4']

# 定义要遍历的文件夹路径
folder_path = '/Users/zhouchen/Desktop/media/videos'

# 获取文件夹下所有视频文件的路径
video_paths = []
for ext in video_extensions:
    video_paths.extend(glob.glob(os.path.join(folder_path, '*' + ext)))

# 遍历所有视频文件，并分割成帧
for video_path in video_paths:
    # 创建一个VideoCapture对象
    cap = cv2.VideoCapture(video_path)

    # 如果无法打开视频，则跳过
    if not cap.isOpened():
        print("Cannot open video:", video_path)
        continue

    # 定义一个变量，表示帧数
    frame_count = 0

    # 循环读取视频帧
    while True:
        # 读取一帧
        ret, frame = cap.read()

        # 如果读取失败，则退出循环
        if not ret:
            break

        # 保存帧
        # 定义输出文件夹路径
        output_folder = os.path.join(folder_path, os.path.splitext(os.path.basename(video_path))[0])

        # 创建输出文件夹
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        out_path = os.path.join(output_folder, "frame%d.jpg" % frame_count)
        print(out_path)
        print(frame)
        cv2.imwrite(out_path, frame)

        # 帧数加1
        frame_count += 1

    # 释放VideoCapture对象
    cap.release()
