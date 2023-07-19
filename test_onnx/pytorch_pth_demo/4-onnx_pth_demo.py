"""
    -*- coding: utf-8 -*-
    @Author: yaofanghao
    @Date: 2023/7/12 11:22
    @Filename: 4-onnx_pth_demo.py
    @Software: PyCharm     
"""

# hrnet.onnx 模型推理，输入图片1x3x480x480，输出480x480x9

import onnx
import numpy as np
import cv2
import onnxruntime as ort

import logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)

# 2023.7.17
# onnxruntime 自定义类
class OnnxProcess():
    def __init__(self, **kwargs):
        self.onnx_model_name = "hrnet-pytorch.onnx"
        self.model = onnx.load(onnx_model_name)
        self.sess = ort.InferenceSession(self.model.SerializeToString())

def load(onnx_model_name):
    logging.info("load onnx")
    # 创建ONNX运行时
    onnx_ = OnnxProcess()
    onnx_.onnx_model_name = "hrnet-pytorch.onnx"
    onnx_.model = onnx.load(onnx_model_name)
    onnx_.sess = ort.InferenceSession(onnx_.model.SerializeToString())

    return onnx_

def onnx_predict(img_name, onnx_):
    logging.info("load image")

    image_size = 480
    # 加载并预处理输入图像
    image = cv2.imread(img_name)
    orininal_h = np.array(image).shape[0]
    orininal_w = np.array(image).shape[1]

    image = cv2.resize(image, (image_size, image_size))
    image = image.astype(np.float32) / 255.0  # 归一化到[0, 1]范围
    image = np.transpose(image, (2, 0, 1))
    image = np.expand_dims(image, axis=0)  # 添加批次维度

    logging.info("start predict")
    # 执行推理
    # input_name = sess.get_inputs()[0].name
    # output_name = sess.get_outputs()[0].name
    input_name = 'images'
    output_name = 'output'
    output = onnx_.sess.run([output_name], {input_name: image})[0]

    # 后处理输出
    output = np.squeeze(output)  # 去除批次维度
    output = np.argmax(output, axis=0)  # 获取每个像素的类别索引

    # 可选：将输出可视化
    class_colors = [(0, 0, 0), (128, 0, 0), (0, 128, 0), (128, 128, 0), (0, 0, 128), (128, 0, 128),
                       (0, 128, 128), (128, 128, 128), (64, 0, 0)] # 类别颜色映射表
    result = np.zeros((image_size, image_size, 3), dtype=np.uint8)
    for i in range(image_size):
        for j in range(image_size):
            result[i, j] = class_colors[output[i, j]]

    result = cv2.resize(result, (orininal_w, orininal_h), interpolation=cv2.INTER_LINEAR)

    logging.info("success!")
    cv2.imshow('Segmentation Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 1

img_name = "5.jpg"
img_name2 = "2304270006.jpg"
img_name3 = "2305190004.jpg"
onnx_model_name = "hrnet-pytorch.onnx"

onnx_ = load(onnx_model_name=onnx_model_name)
onnx_predict(img_name=img_name, onnx_=onnx_)
onnx_predict(img_name=img_name2, onnx_=onnx_)
onnx_predict(img_name=img_name3, onnx_=onnx_)