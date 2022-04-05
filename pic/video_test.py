import sys
import cv2
import os
import math
from sys import platform
import argparse
import numpy as np
import pyopenpose as op
from PIL import Image, ImageDraw, ImageFont

path = 'D:/BaiduNetdiskDownload/openpose1/pic/'
pose_data=np.load("D://BaiduNetdiskDownload//openpose1//pic//data_pose.npy")
type_data=np.load("D://BaiduNetdiskDownload//openpose1//pic//data_type.npy")
pose={'1':'normal','2':'Turn head','3':'Turn body','4':'transmit','5':'sleep'}

# 读取视频文件
videoCapture = cv2.VideoCapture("D:/BaiduNetdiskDownload/openpose1/examples/media/tran.mp4")
# 通过摄像头的方式
#videoCapture=cv2.VideoCapture(1)

# 读帧
success, frame = videoCapture.read()
#print(frame)
i = 0
# 设置固定帧率
timeF = 5
j = 0
params = dict()
params["model_folder"] = "D:\\openpose\\models\\"
# Starting OpenPose
opWrapper = op.WrapperPython()
opWrapper.configure(params)
opWrapper.start()
video=cv2.VideoWriter('D:/BaiduNetdiskDownload/openpose1/images/test.avi',cv2.VideoWriter_fourcc(*'MJPG'),5,(1920,1080))
while success:
    i = i + 1
    if (i % timeF == 0):
        j = j + 1
        test_pose = []
        # Custom Params (refer to include/openpose/flags.hpp for more parameters)
        # Process Image
        datum = op.Datum()
        imageToProcess = frame
        datum.cvInputData = imageToProcess
        opWrapper.emplaceAndPop(op.VectorDatum([datum]))
        # Display Image
        datum.poseKeypoints
        test_pose.append(datum.poseKeypoints[:, :, :2])
        #np.save(path + 'test_pose2', test_pose)
        # print(test_pose)
        test_data = np.squeeze(test_pose)
        # print(test_data)
        KNN = []
        temp = 0
        for v in pose_data:
            p = 0
            for m in range(25):
                p += (test_data[m][0] - v[m][0]) ** 2 + (test_data[m][1] - v[m][1]) ** 2
            d = math.sqrt(p)
            # print(type_data[temp])
            KNN.append([type_data[temp], round(d, 2)])
            temp += 1
        KNN.sort(key=lambda dis: dis[1])
        KNN = KNN[:5]
        v = [x[0] for x in KNN]
        r = max(v, key=v.count)
        for d in pose:
            if r == int(d):
                text = str("pose:%s" % pose[d])
        outdata = cv2.putText(datum.cvOutputData, text, (50, 300), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 4)
        #cv2.namedWindow("OpenPose 1.7.0 - Tutorial Python API", 0)
        #cv2.resizeWindow("OpenPose 1.7.0 - Tutorial Python API", 900, 600)  # 设置窗口大小
        #cv2.imshow("OpenPose 1.7.0 - Tutorial Python API", outdata)
        #cv2.waitKey(0)
        video.write(outdata)
        #save_image(outdata, 'D:/BaiduNetdiskDownload/openpose1/images/', j)
        print('save image:', i)

    success, frame = videoCapture.read()

