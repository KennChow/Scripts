import cv2
import numpy as np

# 定义读取图像的路径和文件名前缀
# img_path = '/Users/zhouchen/Desktop/media/gait_cycle/032-nm-01-090/'
img_path = '/Users/zhouchen/Desktop/media/dataset_display/'

# img_prefix = '032-nm-01-090-0'
img_prefix = ''

# 定义图像的宽度和高度
# img_width = 64
# img_height = 64
img_width = 640
img_height = 480

# 定义一行中图像的数量
num_images_per_row = 5

# 定义要创建的新图像的宽度和高度
new_img_width = img_width * num_images_per_row
new_img_height = img_height

# 创建一个新的图像，用于存储所有的图像
new_img = np.zeros((new_img_height, new_img_width, 3), np.uint8)


# 循环读取每一帧图像
for i in range(11, 16):
    # 构建图像文件名
    img_file = img_path + img_prefix + str(i).zfill(1) + '.jpg'

    print(img_file)

    # 读取图像文件
    img = cv2.imread(img_file)


    # 将图像复制到新的图像中
    x = (i-1) % num_images_per_row * img_width
    y = (i-1) // num_images_per_row * img_height
    print(new_img.shape)
    print('x:' + str(x))
    print('y:' + str(y))
    print(img.shape)
    new_img[0:641, x:x+img_width] = img

    # print(new_img)

# 保存新的图像
cv2.imwrite(img_prefix[0:-1] + '11-15.png', new_img)
