#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:cong
@time: 2024/11/01 09:04:04
"""
import pykinect_azure as pykinect

pykinect.initialize_libraries()
playback = pykinect.start_playback(r"C:\Program Files\Azure Kinect SDK v1.4.1\tools\recorder\output.mkv")
calibration = playback.get_calibration()

# see: https://github.com/microsoft/Azure-Kinect-Sensor-SDK/blob/develop/examples/calibration/main.cpp#L79-L80
resolution_width = calibration._handle.depth_camera_calibration.resolution_width
resolution_height = calibration._handle.depth_camera_calibration.resolution_height
depth_params = calibration.depth_params
message = (
    "Depth Intrinsic parameters: \n"
    f"\tcx: {depth_params.cx}\n"
    f"\tcy: {depth_params.cy}\n"
    f"\tfx: {depth_params.fx}\n"
    f"\tfy: {depth_params.fy}\n"
    f"\tk1: {depth_params.k1}\n"
    f"\tk2: {depth_params.k2}\n"
    f"\tk3: {depth_params.k3}\n"
    f"\tk4: {depth_params.k4}\n"
    f"\tk5: {depth_params.k5}\n"
    f"\tk6: {depth_params.k6}\n"
    f"\tcodx: {depth_params.codx}\n"
    f"\tcody: {depth_params.cody}\n"
    f"\tp2: {depth_params.p2}\n"
    f"\tp1: {depth_params.p1}\n"
    f"\tmetric_radius: {depth_params.metric_radius}\n"
)
print(message)