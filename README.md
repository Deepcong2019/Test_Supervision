数据集下载地址：</br>
UA-DETRAC车辆数据集链接: https://pan.baidu.com/s/15r6bcuFgy79XDvoFD67e0Q?pwd=kz3p 提取码: kz3p </br>

MOT20数据集下载地址：https://motchallenge.net/data/MOT20Det/</br>

车辆检测直接运行：</br>
python .\car_count.py --source_weights_path yolov8m.pt --source_video_path MVI_39031.mp4 --target_video_path test_pred.mp4 --confidence_threshold 0.1</br>
行人检测直接运行：</br>  
python .\person_count.py</br>


尝试使用计算机视觉低代码工具Supervision库：</br>
参考链接：https://www.cnblogs.com/luohenyueji/p/18079658