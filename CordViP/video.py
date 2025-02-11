import cv2

# 读取视频文件
video_path = "static/videos/experiment/pc_video/reach_chicken/output_video1.mp4"  # 替换为你的 MP4 视频路径
cap = cv2.VideoCapture(video_path)

# 检查视频是否成功打开
if not cap.isOpened():
    print("Error: Cannot open video file.")
    exit()

# 读取并显示视频帧
while True:
    ret, frame = cap.read()
    if not ret:
        print("End of video.")
        break

    cv2.imshow("MP4 Video Playback", frame)  # 显示视频窗口

    # 按 'q' 退出
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
