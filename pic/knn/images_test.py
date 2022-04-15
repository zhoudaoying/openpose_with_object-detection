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

try:
    # Import Openpose (Windows/Ubuntu/OSX)
  # Flags
    test_pose=[]
    parser = argparse.ArgumentParser()
    parser.add_argument("--image_path", default="D:\\test_images\\part-00151-2077.jpg", help="Process an image. Read all standard formats (jpg, png, bmp, etc.).")
    args = parser.parse_known_args()
# Custom Params (refer to include/openpose/flags.hpp for more parameters)
    params = dict()
    params["model_folder"] = "D:\\openpose\\models\\"
    # Starting OpenPose
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()
    # Process Image
    datum = op.Datum()
    imageToProcess = cv2.imread(args[0].image_path)
    datum.cvInputData = imageToProcess
    opWrapper.emplaceAndPop(op.VectorDatum([datum]))
    # Display Image
    datum.poseKeypoints
    test_pose.append(datum.poseKeypoints[:, :, :2])
    np.save(path + 'test_pose2', test_pose)
    #print(test_pose)
    test_data = np.squeeze(test_pose)
    #print(test_data)
    KNN = []
    temp = 0
    for v in pose_data:
        p = 0
        for i in range(25):
            p += (test_data[i][0] - v[i][0]) ** 2 + (test_data[i][1] - v[i][1]) ** 2
        d = math.sqrt(p)
        # print(type_data[temp])
        KNN.append([type_data[temp], round(d, 2)])
        temp += 1
    KNN.sort(key=lambda dis: dis[1])
    KNN = KNN[:10]
    v = [x[0] for x in KNN]
    j=max(v,key=v.count)
    for d in pose:
        if j==int(d) :
            text=str("pose:%s"%pose[d])
    outdata=cv2.putText(datum.cvOutputData,text, (50, 300), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 4)
    cv2.namedWindow("OpenPose 1.7.0 - Tutorial Python API", 0)
    cv2.resizeWindow("OpenPose 1.7.0 - Tutorial Python API", 900, 600)  # 设置窗口大小
    cv2.imshow("OpenPose 1.7.0 - Tutorial Python API", outdata)
    cv2.waitKey(0)

except Exception as e:
    sys.exit(-1)


