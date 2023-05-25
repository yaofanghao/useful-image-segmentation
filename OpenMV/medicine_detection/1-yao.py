'''
Author: yao fanghao
Date: 2023-05-23 20:25:34
LastEditTime: 2023-05-23 20:52:12
LastEditors: yao fanghao
'''
# Edge Impulse - OpenMV Object Detection Example

import sensor, image, time, os, tf, math, uos, gc
import time
from pyb import UART

sensor.reset()                         # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565)    # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (320x240)
sensor.set_windowing((240, 240))       # Set 240x240 window.
sensor.skip_frames(time=2000)          # Let the camera adjust.

net = None
labels = None
min_confidence = 0.5

try:
    # load the model, alloc the model file on the heap if we have at least 64K free after loading
    net = tf.load("trained.tflite", load_to_fb=uos.stat('trained.tflite')[6] > (gc.mem_free() - (64*1024)))
except Exception as e:
    raise Exception('Failed to load "trained.tflite", did you copy the .tflite and labels.txt file onto the mass-storage device? (' + str(e) + ')')

try:
    labels = [line.rstrip('\n') for line in open("labels.txt")]
except Exception as e:
    raise Exception('Failed to load "labels.txt", did you copy the .tflite and labels.txt file onto the mass-storage device? (' + str(e) + ')')

colors = [ # Add more colors if you are detecting more than 7 types of classes at once.
    (255,   0,   0),
    (  0, 255,   0),
    (255, 255,   0),
    (  0,   0, 255),
    (255,   0, 255),
    (  0, 255, 255),
    (255, 255, 255),
]


## 2023.5.23 yaofanghao 按行读取txt
_classes_gbk_txt = "dic_gbk.txt"  # 分类标签文件中文版
def read_txt_lines(_classes_gbk_txt=None):
    __name_classes_gbk = []
    f_gbk = open(_classes_gbk_txt, "r", encoding='utf-8')
    lines_gbk = f_gbk.read().splitlines()
    for i in range(len(lines_gbk)):
        __name_classes_gbk.append(lines_gbk[i])
    return __name_classes_gbk

clock = time.clock()
while(True):
    clock.tick()

    uart = UART(3, 19200)
    #uart.write("Hello World!\r")
    #time.sleep_ms(1000)


    img = sensor.snapshot()

    for i, detection_list in enumerate(net.detect(img, thresholds=[(math.ceil(min_confidence * 255), 255)])):
        if (i == 0): continue # background class
        if (len(detection_list) == 0): continue # no detections for this class?


        # 2023.5.23 读取标签和中文标签
        _name_classes_gbk = read_txt_lines(_classes_gbk_txt=_classes_gbk_txt)

        print("********** %s **********" % labels[i])
        for d in detection_list:
            [x, y, w, h] = d.rect()
            #center_x = math.floor(x + (w / 2))
            #center_y = math.floor(y + (h / 2))
            #print('x %d\ty %d' % (center_x, center_y))
            print('x %d\ty %d\t w %d\th %d\n' % (x,y,w,h))
            print("********** %s **********\n" % _name_classes_gbk[i])
            uart.write('x %d\ty %d\t w %d\th %d \n' % (x,y,w,h))
            uart.write("********** %s **********\n" % _name_classes_gbk[i])
            img.draw_rectangle(x, y, w, h, color = colors[i], thickness = 2)