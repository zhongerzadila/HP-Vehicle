import os
import random
import shutil

def moveFile(imgs_Dir, labels_Dir):
        # 训练集路径
        train_img_Dir = '/home/zhang/zengjunqi/parkinglot_occupancy/parkinglot_dataset/2022_11_19/train/images/'
        train_label_Dir = '/home/zhang/zengjunqi/parkinglot_occupancy/parkinglot_dataset/2022_11_19/train/labels/'
        # 验证集路径
        val_img_Dir = '/home/zhang/zengjunqi/parkinglot_occupancy/parkinglot_dataset/2022_11_19/valid/images/'
        val_label_Dir = '/home/zhang/zengjunqi/parkinglot_occupancy/parkinglot_dataset/2022_11_19/valid/labels/'
        # 测试集路径
        test_img_Dir = '/home/zhang/zengjunqi/parkinglot_occupancy/parkinglot_dataset/2022_11_19/test/images/'
        test_label_Dir = '/home/zhang/zengjunqi/parkinglot_occupancy/parkinglot_dataset/2022_11_19/test/labels/'
        img_pathDir = os.listdir(imgs_Dir)
        print("img_pathDir:{}".format(img_pathDir))# 提取图片的原始路径
        filenumber = len(img_pathDir)
        # 自定义训练集的数据比例
        train_rate = 0.7                                            # 如0.2，就是20%的意思
        train_picknumber = int(filenumber*train_rate)                # 按照train_rate比例从文件夹中取一定数量图片
        # 自定义val的数据比例
        val_rate = 0.25
        val_picknumber = int(filenumber*val_rate)                  # 按照val_rate比例从文件夹中取一定数量图片
        # 自定义test的数据比例
        test_rate = 0.05
        test_picknumber = int(filenumber * test_rate)  # 按照val_rate比例从文件夹中取一定数量图片
        # 选取移动到train中的样本
        sample1 = random.sample(img_pathDir, train_picknumber)      # 随机选取picknumber数量的样本图片
        for i in range(0, len(sample1)):
            sample1[i] = sample1[i][:-4]                           # 去掉图片的拓展名，移动标注时需要这个列表
        for name in sample1:
            src_img_name1 = imgs_Dir + name
            dst_img_name1 = train_img_Dir + name
            shutil.copy(src_img_name1 + '.jpg', dst_img_name1 + '.jpg')     # 加上图片的拓展名，移动图片
            src_label_name1 = labels_Dir + name
            dst_label_name1 = train_label_Dir + name
            shutil.copy(src_label_name1 + '.txt', dst_label_name1 + '.txt')   # 加上标注文件的拓展名，移动标注文件
        # 选取移动到val中的样本
        sample2 = random.sample(img_pathDir, val_picknumber)       # 但是抽出来的数目，还是用之前算的
        print(sample2)
        for i in range(0, len(sample2)):
            sample2[i] = sample2[i][:-4]
        for name in sample2:
            src_img_name2 = imgs_Dir + name
            dst_img_name2 = val_img_Dir + name
            shutil.copy(src_img_name2 + '.jpg', dst_img_name2 + '.jpg')
            src_label_name2 = labels_Dir + name
            dst_label_name2 = val_label_Dir + name
            shutil.copy(src_label_name2 + '.txt', dst_label_name2 + '.txt')

        # 选取移动到test中的样本
        sample3 = random.sample(img_pathDir, test_picknumber)  # 但是抽出来的数目，还是用之前算的
        print(sample3)
        for i in range(0, len(sample3)):
            sample3[i] = sample3[i][:-4]
        for name in sample3:
            src_img_name3 = imgs_Dir + name
            dst_img_name3 = test_img_Dir + name
            shutil.copy(src_img_name3 + '.jpg', dst_img_name3 + '.jpg')
            src_label_name3 = labels_Dir + name
            dst_label_name3 = test_label_Dir + name
            shutil.copy(src_label_name3 + '.txt', dst_label_name3 + '.txt')
        return

if __name__ == '__main__':
    # 从images中移动
    imgs_Dir = '/home/zhang/zengjunqi/parkinglot_occupancy/parkinglot_dataset/2022_11_19/images/'
    labels_Dir = '/home/zhang/zengjunqi/parkinglot_occupancy/parkinglot_dataset/2022_11_19/labels/'
    # 运行划分数据集函数
    moveFile(imgs_Dir, labels_Dir)

