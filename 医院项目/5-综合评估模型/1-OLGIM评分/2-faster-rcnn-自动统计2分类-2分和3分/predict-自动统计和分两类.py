 # 2023.4.8 @yaofanghao 只有2分和3分的模型，统计二分类结果
import numpy
from PIL import Image
import os
from frcnn import FRCNN

########### 设置区域 ###########
dir_origin_path = "test/"  # 输入图片文件夹路径

if __name__ == "__main__":
    frcnn = FRCNN()

    dir_save_path = "img_out"

    # 存放全部图片预测结果数据的txt
    f1 = open(os.path.join(os.getcwd(), 'predict_result.txt'), 'a')

    # all_save_path_0 = str(dir_save_path) + "_0-1/"
    all_save_path_2 = str(dir_save_path) + "_2/"
    all_save_path_3 = str(dir_save_path) + "_3/"
    all_save_path_none = str(dir_save_path) + "_none/"
    # if not os.path.exists(all_save_path_0):
    #     os.makedirs(all_save_path_0)
    if not os.path.exists(all_save_path_2):
        os.makedirs(all_save_path_2)
    if not os.path.exists(all_save_path_3):
        os.makedirs(all_save_path_3)
    if not os.path.exists(all_save_path_3):
        os.makedirs(all_save_path_3)
    if not os.path.exists(all_save_path_none):
        os.makedirs(all_save_path_none)

    # 统计识别为各类的个数
    # num0 = 0
    num2 = 0
    num3 = 0
    none = 0

    img_names = os.listdir(dir_origin_path)
    # img_names.sort(key=lambda x:int(x.split('.')[0]))  # 按照1，2，3顺序读图片
    for img_name in img_names:
        if img_name.lower().endswith(
                ('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
            image_path = os.path.join(dir_origin_path, img_name)
            image = Image.open(image_path)
            print(img_name)

            # 修改detect_image 的返回值
            r_image, out_scores, out_classes,top,right, left,bottom= frcnn.detect_image(image)

        # -----------------------------------------------------------------------------------------------#
            out_scores_size = out_scores.size
            # print('------------------')
            print(out_scores)
            print(out_classes)
            f1.write(img_name)
            f1.write("\r")
            out_scores = numpy.around(out_scores,3)

            if out_scores[0]==0:  # 2023.3.2 解决了部分图片non-iterable的错误问题
                none += 1
                r_image.save(os.path.join(all_save_path_none, img_name.replace(".jpg", ".png")), quality=95, subsampling=0)
                f1.write("置信度分数最大的类别为：none")
                f1.write("\r")
                f1.write("分数为：none")
                f1.write("\r")
                f1.write("-------------------")
                f1.write("\r")

            if (out_scores.size != 0) & (out_scores[0]>0):
                ################ 找到置信度最大的类别的算法 ############
                num = 0
                t = out_scores
                # class0 = numpy.array([0])
                class2 = numpy.array([0])
                class3 = numpy.array([0])

                for i in out_classes:
                    # if i == 0:
                    #     class0 = numpy.append(class0, t[num])
                    if i == 0:
                        class2 = numpy.append(class2, t[num])
                    if i == 1:
                        class3 = numpy.append(class3, t[num])
                    num += 1

                # class0_max = numpy.max(class0)
                # class0_max=round(class0_max, 4)
                class2_max = numpy.max(class2)
                class2_max=round(class2_max, 4)
                class3_max = numpy.max(class3)
                class3_max=round(class3_max, 4)

                locat = out_scores.argmax(axis=None, out=None)  # 找最大值位置
                out_scores_max = out_scores.max()
                out_scores_max =round(out_scores_max,4)   # 小数点后2位
                a = out_classes
                class_max_confidence = a[locat]  # 最大值位置的类别
                print(class_max_confidence)

                if class_max_confidence == 0:
                    class_max_confidence = '2'
                    num2 += 1
                    r_image.save(os.path.join(all_save_path_2, img_name.replace(".jpg", ".png")),quality=95, subsampling=0)
                if class_max_confidence == 1:
                    class_max_confidence = '3'
                    num3 += 1
                    r_image.save(os.path.join(all_save_path_3, img_name.replace(".jpg", ".png")),quality=95, subsampling=0)

                f1.write("置信度分数最大的类别为："+str(class_max_confidence))
                f1.write("\r")
                f1.write("分数为："+str(out_scores_max))
                f1.write("\r")
                f1.write("-------------------")
                f1.write("\r")

    # # -----------------------------------------------------------------------------------------------#
    rate_2 = (num2 / (num2+num3+none)) *100
    rate_3 = (num3 / (num2+num3+none)) *100
    rate_none = (none / (num2 + num3 + none)) * 100

    print("识别为2分：", num2)
    print("识别为3分：", num3)
    print("无结果：", none)
    print("识别为2分的比例：", str(rate_2) + '%')
    print("识别为3分的比例：", str(rate_3) + '%')
    print("无结果的比例：", str(rate_none) + '%')

    f1.close()
    f = open(os.path.join(os.getcwd(), 'predict_report.txt'), 'a')
    f.write("识别为2分：" + str(num2))
    f.write("\r")
    f.write("识别为3分：" + str(num3))
    f.write("\r")
    f.write("无结果：" + str(none))
    f.write("\r")
    f.write("识别为2分的比例：" + str(rate_2) + '%')
    f.write("\r")
    f.write("识别为3分的比例：" + str(rate_3) + '%')
    f.write("\r")
    f.write("无结果的比例：" + str(rate_none) + '%')
    f.write("\r")
    f.close()

