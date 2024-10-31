#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:cong
@time: 2024/10/31
"""

import cv2
import numpy as np
import supervision as sv
from ultralytics import YOLO
from tqdm import tqdm
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

source_video_path = "img1.mp4"
target_video_path = "test_person.mp4"
model = YOLO("yolov8n.pt")
classes = list(model.names.values())  # Class names
frame_generator = sv.get_video_frames_generator(source_video_path)  # for generating frames from video
video_info = sv.VideoInfo.from_video_path(video_path=source_video_path)
tracker = sv.ByteTrack()

label_annotator = sv.LabelAnnotator()  # Label annotator instance

with sv.VideoSink(target_path=target_video_path, video_info=video_info) as sink:
    for frame in tqdm(frame_generator, total=video_info.total_frames):
        # Getting result from model
        results = model(frame, verbose=False, conf=0.3, iou=0.7)[0]
        detections = sv.Detections.from_ultralytics(results)  # Getting detections
        print("count: ", len(detections))
        # Filtering classes for car and truck only instead of all COCO classes.
        detections = detections[np.where(detections.class_id == 0)]
        detections = tracker.update_with_detections(detections)  # Updating detection to Bytetracker

        # corner_length-每个角线的长度，
        corner_annotator = sv.BoxCornerAnnotator(corner_length=12, color=sv.Color(r=255, g=255, b=0))
        annotated_frame = corner_annotator.annotate(
            scene=frame.copy(),
            detections=detections
        )
        #sv.plot_image(annotated_frame)
        # Prepare labels
        labels = []
        for index in range(len(detections.class_id)):
            # creating labels as per required.
            labels.append(
                "#" + str(detections.tracker_id[index]) + " " + classes[detections.class_id[index]] + " " + str(
                    round(detections.confidence[index], 2)))


        # Annotating labels
        annotated_label_frame = label_annotator.annotate(scene=annotated_frame, detections=detections,
                                                         labels=labels)
        # Annotating line labels
        sink.write_frame(frame=annotated_label_frame)


