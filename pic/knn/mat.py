import sys
import numpy as np
import math
import matplotlib.pyplot as plt
pose_data=np.load("D://BaiduNetdiskDownload//openpose1//pic//data_pose.npy")
type_data=np.load("D://BaiduNetdiskDownload//openpose1//pic//data_type.npy")
test_data_pose=np.load("D://BaiduNetdiskDownload//openpose1//pic//test_data_pose.npy")
test_data_type=np.load("D://BaiduNetdiskDownload//openpose1//pic//test_data_type.npy")
ktemp = 0
grade = 0
for x in test_data_pose:
    KNN = []
    temp = 0
    for v in pose_data:
        p = 0
        for i in range(25):
            p += (x[i][0] - v[i][0]) ** 2 + (x[i][1] - v[i][1]) ** 2
        d = math.sqrt(p)
        # print(type_data[temp])
        KNN.append([type_data[temp], round(d, 2)])
        temp += 1
    KNN.sort(key=lambda dis: dis[1])
    KNN = KNN[:5]
    v = [x[0] for x in KNN]
    # print(v)
    # print(test_data_type[ktemp])
    j = max(v, key=v.count)
    if j == test_data_type[ktemp]:
        print("预测正确")
        grade += 1
    else:
        pass
        print("预测错误，应为：",test_data_type[ktemp])
    ktemp += 1
g = grade / 123
print('训练集正确率为：{:.2f}%'.format(g * 100))
