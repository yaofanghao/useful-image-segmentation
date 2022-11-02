# coding:utf-8
import sys
import cv2
import numpy as np
import os

# 设置图片路径
DATADIR = r"E:\MyGithub\cannytest\3-suanfa2"
output_dir_canny = r"E:\MyGithub\cannytest\4-canny\\"
output_dir_juxing = r"E:\MyGithub\cannytest\5-juxing\\"
output_dir_suanfa5 = r"E:\MyGithub\cannytest\6-suanfa5\\"
if not os.path.exists(output_dir_canny):
    os.makedirs(output_dir_canny)
if not os.path.exists(output_dir_juxing):
    os.makedirs(output_dir_juxing)
if not os.path.exists(output_dir_suanfa5):
    os.makedirs(output_dir_suanfa5)

# 使用os.path模块的join方法生成路径'''
path = os.path.join(DATADIR)
img_list = os.listdir(path)

img_list.sort(key=lambda x:int(x[:-4]))

ind = 1
for i in img_list:
    # 图片文件名称，和代码放在了同一文件夹下
    pathjpg = os.path.join(path, i)
    print(pathjpg)

    img = cv2.imread(pathjpg, cv2.IMREAD_COLOR)  # 读取指定位置的彩色图像

    # opencv读取灰度图像
    img = cv2.imread(pathjpg, 1)

    #-----------------
    # canny(): 边缘检测
    img1 = cv2.GaussianBlur(img, (1, 1), 0)
    canny = cv2.Canny(img1, 1, 150)

    # 形态学：边缘检测
    _, Thr_img = cv2.threshold(img, 210, 255, cv2.THRESH_BINARY)  # 设定红色通道阈值210（阈值影响梯度运算效果）
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 定义矩形结构元素
    gradient = cv2.morphologyEx(Thr_img, cv2.MORPH_GRADIENT, kernel)  # 梯度

    save_path_canny = output_dir_canny + str((ind)) + '.jpg'
    cv2.imwrite(save_path_canny, canny)
    print(save_path_canny)

    ###        边缘检测得出x，y坐标
    Ymax = 200
    Ymin = 200
    Xmax = 200
    Xmin = 200
    img_path = save_path_canny
    # 读取文件
    mat_img = cv2.imread(img_path)
    mat_img2 = cv2.imread(img_path, cv2.CV_8UC1)

    # 自适应分割
    dst = cv2.adaptiveThreshold(mat_img2, 210, cv2.BORDER_REPLICATE, cv2.THRESH_BINARY_INV, 3, 10)
    # 提取轮廓
    _, contours, heridency = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 标记轮廓
    cv2.drawContours(mat_img, contours, -1, (255, 0, 255), 3)

    max_area = -1
    for i in range(len(contours)):
        area = cv2.contourArea(contours[i])
        if area > max_area:
            cnt = contours[i]
            max_area = area

    # 计算轮廓面积
    Area = 0
    for i in contours:
        area = cv2.contourArea(i)
        if (Area < area):
            Area = area

    Hmax = 0
    Wmax = 0
    if len(contours) > 0:
        # cv2.boundingRect()返回轮廓矩阵的坐标值，四个值为x, y, w, h， 其中x, y为左上角坐标，w,h为矩阵的宽和高
        boxes = [cv2.boundingRect(c) for c in contours]
        for box in boxes:
            x, y, w, h = box
            if (Hmax < h):
                Hmax = h
                Ymin = y
                Ymax = y + Hmax
            if (Wmax < w):
                Wmax = w
                Xmin = x
                Xmax = x + Wmax
            # 绘制矩形框对轮廓进行定位
            cv2.rectangle(mat_img, (x, y), (x + w, y + h), (153, 153, 0), 2)
    file = open(r'text2.txt', mode='a')  # 将空格写入txt文件中
    file.write(' ')
    file.write(str(Ymin))
    file.write(' ')
    file.write(str(Ymax))
    file.write(' ')
    file.write(str(Xmin))
    file.write(' ')
    file.write(str(Xmax))
    file.write(' ')
    file.write('\n')  # 将回车写入txt文件中
    file.close()

    save_path_juxing = output_dir_juxing + str((ind)) + '.jpg'  # 保存至另一文件夹
    cv2.imwrite(save_path_juxing, mat_img)

    img_name1 = str(ind) + '.jpg'
    ##剪原图jpg
    img = cv2.imread(pathjpg)
    cropped = img[Ymin:Ymax, Xmin:Xmax]  # 裁剪坐标为[y0:y1, x0:x1]
    save_path = output_dir_suanfa5 + str(ind) + '.jpg'
    cv2.imwrite(save_path, cropped)
    #cv2.waitKey(0)

    ind += 1
