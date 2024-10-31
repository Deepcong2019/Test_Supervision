#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:cong
@time: 2024/10/31 15:36:20
"""
import re

import cv2
import os


def images_to_video(image_folder: str, output_video_path: str, frame_rate: int = 25):
    # 获取文件夹中的所有图片文件
    images = [img for img in os.listdir(image_folder) if img.endswith(('.png', '.jpg', '.jpeg'))]

    # 按文件名排序，以确保图片按顺序添加到视频中
    images.sort()

    if not images:
        print("没有找到任何图片.")
        return

    # 读取第一张图片获取宽高信息
    image_path = os.path.join(image_folder, images[0])
    first_image = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = first_image.shape

    # 定义视频编码和输出视频文件
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 可以使用不同的编码器，如 'XVID', 'mp4v', 'MJPG'
    video = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (width, height))

    # 遍历所有图片并写入视频文件
    count = 0
    for image in images:
        count += 1
        if count < 100:
            img = cv2.imread(os.path.join(image_folder, image))
            video.write(img)  # 将图像写入视频

    video.release()  # 释放视频文件
    cv2.destroyAllWindows()  # 关闭所有OpenCV窗口


# 示例使用
if __name__ == "__main__":
    image_folder = r'E:\JA_DATA\MOT20Det\train\MOT20-02\img1'  # 替换为你的图片文件夹路径
    video_name = re.split(r'[\\\/]', image_folder)[-1] + '.mp4'
    images_to_video(image_folder, video_name)
