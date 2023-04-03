import pyrealsense2 as rs
import numpy as np
import cv2

if __name__ == "__main__":
    # Configure depth and color streams
    ctx = rs.context()
    print(ctx.devices)
    frameSize = (640, 480)
    fps = 30
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    filename = input("请输入视频文件名称:")
    video_writer = cv2.VideoWriter(filename=filename, fourcc=fourcc, fps=fps, frameSize=(640, 480))  # 大小要和图片实际大小一样

    pipeline = rs.pipeline()
    config = rs.config()
    # config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
    config.enable_stream(rs.stream.color, frameSize[0], frameSize[1], rs.format.bgr8, fps)
    # Start streaming
    pipeline.start(config)
    cnt = 0
    capFlag = False
    try:
        while True:
            # Wait for a coherent pair of frames: depth and color
            frames = pipeline.wait_for_frames()
            # depth_frame = frames.get_depth_frame()
            color_frame = frames.get_color_frame()
            if not depth_frame or not color_frame:
                continue
            # Convert images to numpy arrays

            # depth_image = np.asanyarray(depth_frame.get_data())

            color_image = np.asanyarray(color_frame.get_data())
            cnt += 1

            # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
            # depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)
            # Stack both images horizontally
            # images = np.hstack((color_image, depth_colormap))
            images = color_image
            # Show images
            cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
            cv2.imshow('RealSense', images)
            key = cv2.waitKey(1)

            if key & 0xFF == ord('s'):
                capFlag = True
            if capFlag:
                cv2.imwrite(str(cnt) + '.jpg', color_image)
                # img = cv2.imread(filename=str(cnt) + '.jpg')
                # cv2.waitKey(100)
                video_writer.write(color_image)

            # Press esc or 'q' to close the image window
            if key & 0xFF == ord('q') or key == 27 or cnt == 500:
                cv2.destroyAllWindows()
                break
    finally:
        # Stop streaming
        pipeline.stop()
