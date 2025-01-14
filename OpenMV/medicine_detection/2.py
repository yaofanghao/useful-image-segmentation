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

     
def txt_read(files):
    txt_dict = {}
    fopen = open(files)
    for line in fopen.readlines():
        line = str(line).replace("\n","") #注意，必须是双引号，找了大半个小时，发现是这个问题。。
        txt_dict[line.split(' ',1)[0]] = line.split(' ',1)[1]
        #split（）函数用法，逗号前面是以什么来分割，后面是分割成n+1个部分，且以数组形式从0开始
    fopen.close()
    return txt_dict

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

        # print("22222")


        print("********** %s **********" % labels[i])
        for d in detection_list:
            [x, y, w, h] = d.rect()
            #center_x = math.floor(x + (w / 2))
            #center_y = math.floor(y + (h / 2))
            #print('x %d\ty %d' % (center_x, center_y))
            print('x %d\ty %d\t w %d\th %d' % (x,y,w,h))
            uart.write('x %d\ty %d\t w %d\th %d \n' % (x,y,w,h))
            uart.write("********** %s **********\n" % labels[i])
            img.draw_rectangle(x, y, w, h, color = colors[i], thickness = 2)
            #img.draw_circle((center_x, center_y, 12), color=colors[i], thickness=2)

txt_dict = txt_read('dic.txt')
print(txt_dict)