# ViT 参考资料
* 更新时间 8.23

## 本代码
  * **修改内容**
    * 8.23 predict.py 批量预测并分类至对应文件夹
  * 参考来源： https://www.bilibili.com/video/BV1q64y1X7GY
  * **模型训练：设置好以后运行train.py即可**
    * data_root为数据集的根目录，包含每种类型图片的文件夹
    * 根据需要调整参数如 batch_size、epochs、num_classes、freeze_layers、initial_lr、weight_decay 
    * **pre_weights_path = './ViT-B_16.h5'** 通常不用修改，其他模型运算量太大
  * **模型预测：设置好以后运行predict.py即可**
    * 有关参数需要和train.py对应，比如has_logit都为False等



## 其他资料
* https://www.bilibili.com/video/BV15P4y137jb?share_source=copy_web
* https://zhuanlan.zhihu.com/p/445122996
* https://www.bilibili.com/video/BV1q64y1X7GY
* https://www.bilibili.com/video/BV1aF411b7WW?share_source=copy_web
* paddle开源代码 
  * https://github.com/BR-IDL/PaddleViT