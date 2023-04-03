from moviepy.editor import VideoFileClip, concatenate_videoclips

# 视频文件名
video1 = 'video1.mp4'
video2 = 'video2.mp4'
video3 = 'video3.mp4'

# 加载视频片段
clip1 = VideoFileClip("125-nm-23-090.mp4")
clip2 = VideoFileClip("130-nm-22-090.mp4")
clip3 = VideoFileClip("133-nm-30-090.mp4")

# 合并视频
final_clip = concatenate_videoclips([clip1, clip2, clip3])

# 生成输出视频文件
final_clip.write_videofile('output.mp4')
