from PIL import Image

# 读取图像文件
image = Image.open("052-nm-03-090-048.png")

# 裁剪图像
cropped_image = image.crop((10, 0, 54, 64))

# 保存裁剪后的图像文件
cropped_image.save("052-nm-03-090-048-cut.png")
