# import json
# import os


# def convert(img_size, box):
#     x1 = box[0]
#     y1 = box[1]
#     x2 = box[2]
#     y2 = box[3]

#     center_x = (x1 + x2) * 0.5 / img_size[0]
#     center_y = (y1 + y2) * 0.5 / img_size[1]
#     w = abs((x2 - x1)) * 1.0 / img_size[0]
#     h = abs((y2 - y1)) * 1.0 / img_size[1]

#     return (center_x, center_y, w, h)


# def convert1(img_size, box):
#     x1 = box[0]
#     y1 = box[1]

#     center_x = x1 / img_size[0]
#     center_y = y1 / img_size[1]

#     return (center_x, center_y)


# def decode_json(jsonfloder_path, json_name):
#     txt_name = '/home/zhang/zengjunqi/videos/parkinglot_dataset/train/labels_yolov5/' + json_name[0:-5] + '.txt'
#     # txt保存位置

#     txt_file = open(txt_name, 'w')  # te files

#     json_path = os.path.join(json_folder_path, json_name)
#     data = json.load(open(json_path, 'r'))

#     img_w = data['imageWidth']
#     img_h = data['imageHeight']
#     for i in data['shapes']:
#         if (i['shape_type'] == 'rectangle'):  # 仅适用矩形框标注
#             x1 = float(i['points'][0][0])
#             y1 = float(i['points'][0][1])
#             x2 = float(i['points'][1][0])
#             y2 = float(i['points'][1][1])
#             if x1 < 0 or x2 < 0 or y1 < 0 or y2 < 0:
#                 continue
#             else:
#                 bb = (x1, y1, x2, y2)
#                 bbox = convert((img_w, img_h), bb)
#             if i['label'] == "jc_re":
#                 txt_file.write("0 " + " ".join([str(a) for a in bbox])+" ")
#             # elif i['label'] == "jc_point":
#             # txt_file.write("1 " + " ".join([str(a) for a in bbox]) + '\n')
#             # elif i['label'] == "Computer":
#             # txt_file.write("2 " + " ".join([str(a) for a in bbox]) + '\n')
#             # else:
#             # txt_file.write("3 " + " ".join([str(a) for a in bbox]) + '\n')
#         elif (i['shape_type'] == 'point'):  # 适用点标注

#             x1 = float(i['points'][0][0])
#             y1 = float(i['points'][0][1])
#             if x1 < 0 or y1 < 0:
#                 continue
#             else:
#                 bb = (x1, y1)
#                 bbox = convert1((img_w, img_h), bb)
#             if i['label'] == "jc_point":
#                 # txt_file.write(" ".join([str(a) for a in bbox]) + "\n")
#                 txt_file.write(" ".join([str(a) for a in bbox])+" ")


# if __name__ == "__main__":

#     json_folder_path = '/home/zhang/zengjunqi/videos/parkinglot_dataset/train/labels/'  # json文件夹路径
#     json_names = os.listdir(json_folder_path)  # file name
#     for json_name in json_names:  # output all files
#         if json_name[-5:] == '.json':  # just work for json files
#             decode_json(json_folder_path, json_name)


# 实现json文件yolov5训练的txt文件
# 注意：图像的宽高需要自定义


# import json
# import os


# def convert(img_size, box):
#     x1 = box[0]
#     y1 = box[1]
#     x2 = box[2]
#     y2 = box[3]

#     # 转换并归一化
#     center_x = (x1 + x2) * 0.5 / img_size[0]
#     center_y = (y1 + y2) * 0.5 / img_size[1]
#     w = abs((x2 - x1)) * 1.0 / img_size[0]
#     h = abs((y2 - y1)) * 1.0 / img_size[1]

#     return (center_x, center_y, w, h)



# def decode_json(save_path, jsonfloder_path, json_name, classes):
#     txt_name = save_path + json_name[0:-5] + '.txt'
#     # txt保存位置

    
#     json_path = os.path.join(json_folder_path, json_name)
#     data = json.load(open(json_path, 'r'))

#     img_w = 1280
#     img_h = 720
#     with open(txt_name, 'w') as txt_file:  # te files
#         for i in data['labels']:
#             if i['box2d']:  # 仅适用矩形框标注
#                 x1 = float(i['box2d']['x1'])
#                 y1 = float(i['box2d']['y1'])
#                 x2 = float(i['box2d']['x2'])
#                 y2 = float(i['box2d']['y2'])
#                 if x1 < 0 or x2 < 0 or y1 < 0 or y2 < 0:
#                     continue
#                 else:
#                     bb = (x1, y1, x2, y2)
#                     bbox = convert((img_w, img_h), bb)
                
#                 cls = i['category']  # 得到当前label的类别
                
#                 # 转换成训练模式读取的标签
#                 cls_id = classes.index(cls)  # 位于定义类别索引位置
                
#                 # 保存
#                 txt_file.write(str(cls_id) + ' ' +" ".join([str(a) for a in bbox])+"\n")  # 生成格式0 cx,cy,w,h
            
       


# if __name__ == "__main__":

#     # 数据的类别
#     classes_train = ["space-occupied","space-empty"]   # 修改1，类别

#     json_folder_path = '/home/zhang/zengjunqi/videos/parkinglot_dataset/train/labels/'  # 修改2，json文件夹路径，
#     save_path = '/home/zhang/zengjunqi/videos/parkinglot_dataset/train/labels_yolov5/'    # 修改3，保存位置

#     json_names = os.listdir(json_folder_path)  # file name
    
#     # 遍历所有json文件
#     for json_name in json_names:  # output all files
#         if json_name[-5:] == '.json':  # just work for json files
#             decode_json(save_path, json_folder_path, json_name, classes_train)


import os
import json
import numpy as np
# 类和索引
CLASSES=["space-occupied","space-empty"]
def convert(size,box):
    '''
    input:
    size:(width,height);
    box:(x1,x2,y1,y2)
    output:
    (x,y,w,h)
    '''
    dw=1./size[0]
    dh=1./size[1]
    x=(box[0]+box[1])/2.0
    y=(box[2]+box[3])/2.0
    w=box[1]-box[0]
    h=box[3]-box[2]
    x=x*dw
    w=w*dw
    y=y*dh
    h=h*dh
    return (x,y,w,h)
# json -> txt
def json2txt(path_json,path_txt):
    with open(path_json,"r") as path_json:
        jsonx=json.load(path_json)
        width=int(jsonx["imageWidth"])      # 原图的宽
        height=int(jsonx["imageHeight"])    # 原图的高
        with open(path_txt,"w+") as ftxt:
            # 遍历每一个bbox对象
            for shape in jsonx["shapes"]:
                obj_cls=str(shape["label"])     # 获取类别
                cls_id=CLASSES.index(obj_cls)   # 获取类别索引
                points=np.array(shape["points"])    # 获取(x1,y1,x2,y2)
                x1=int(points[0][0])
                y1=int(points[0][1])
                x2=int(points[1][0])
                y2=int(points[1][1])
                # (左上角,右下角) -> (中心点,宽高) 归一化
                bb=convert((width,height),(x1,x2,y1,y2))
                ftxt.write(str(cls_id)+" "+" ".join([str(a) for a in bb])+"\n")
if __name__=="__main__":
    # json文件夹
    dir_json="/home/zhang/zengjunqi/parkinglot_occupancy/parkinglot_dataset/2022_11_19/labels/"
    # txt文件夹
    dir_txt="/home/zhang/zengjunqi/parkinglot_occupancy/parkinglot_dataset/2022_11_19/labels_yolov5/"
    if not os.path.exists(dir_txt):
        os.makedirs(dir_txt)
    # 得到所有json文件
    list_json=os.listdir(dir_json)
    # 遍历每一个json文件,转成txt文件
    for cnt,json_name in enumerate(list_json):
        print("cnt=%d,name=%s"%(cnt,json_name))
        path_json=dir_json+json_name
        path_txt=dir_txt+json_name.replace(".json",".txt")
        # (x1,y1,x2,y2)->(x,y,w,h)
        json2txt(path_json,path_txt) 