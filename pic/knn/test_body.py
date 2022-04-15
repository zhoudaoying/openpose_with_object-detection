import sys
import cv2
import os
from sys import platform
import argparse
import pyopenpose as op
#本次实验均由本人独立完成
try:
    parser = argparse.ArgumentParser()
    #设置图片路径
    parser.add_argument("--image_path", default="D:/BaiduNetdiskDownload/openpose1/examples/media/qqq.jpg")
    args = parser.parse_known_args()
    params = dict()
    params["model_folder"] = "D:\\openpose\\models\\"
    # 启动OpenPose
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()
    # 加载图片
    datum = op.Datum()
    imageToProcess = cv2.imread(args[0].image_path)
    datum.cvInputData = imageToProcess
    opWrapper.emplaceAndPop(op.VectorDatum([datum]))
    # 图片展示
    print("Body keypoints: \n" + str(datum.poseKeypoints))  #打印人体关节点信息
    cv2.namedWindow("OpenPose 1.7.0 - Tutorial Python API", 0)
    cv2.resizeWindow("OpenPose 1.7.0 - Tutorial Python API", 900, 600)  # 设置窗口大小
    cv2.imshow("OpenPose 1.7.0 - Tutorial Python API", datum.cvOutputData)
    cv2.waitKey(0)
except Exception as e:
    print(e)
    sys.exit(-1)