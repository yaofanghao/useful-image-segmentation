# 2023.3.2 @yaofanghao
# 把胃窦胃体图片所有子文件夹下的图片提取到一个output文件夹中
# 分不清循环的时候debug一下，看各变量名即可

# coding=utf-8
import os
import shutil

#目标文件夹路径
determination = './output'
if not os.path.exists(determination):
    os.makedirs(determination)

#原文件夹总的路径
path = './source'
folders = os.listdir(path)
for folder in folders:
    dirs = path + '/' + str(folder)
    dirs_dir = os.listdir(dirs)
    for dir in dirs_dir:
        files = path + '/' + str(folder) + '/' + str(dir)
        files_file = os.listdir(files)
        for file in files_file:
            source = files + '/' + str(file)
            deter = determination + '/' + str(file)
            print("source:", source)
            print("deter:", deter)
            shutil.copyfile(source, deter)
