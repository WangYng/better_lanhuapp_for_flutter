# This is a sample Python script.

import os
import re
import shutil
import zipfile

# 检测文件名是否包含中文字符,
from env import download_dir, project_image_dir, project_code_file


def contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


# 字符转下划线驼峰
def down_line_to_hump(text):
    arr = re.split('[-_ ]', text)
    res = ''
    j = 0
    for i in arr:
        if j == 0:
            res = i[0].upper() + i[1:].lower()
        else:
            res = res + '_' + i[0].upper() + i[1:].lower()
        j += 1
    return res


# 检查是否是蓝湖的图片文件
def is_lanhu_zip(file_path):
    zip_obj = zipfile.ZipFile(file_path, 'r')
    name_list = zip_obj.namelist()
    zip_obj.close()

    scale_1_image = ''
    scale_2_image = ''
    scale_3_image = ''

    if len(name_list) >= 3:
        for name in name_list:
            if name.endswith('@3x.png'):
                scale_3_image = name
            elif name.endswith('@2x.png'):
                scale_2_image = name
            elif name.endswith('.png'):
                scale_1_image = name
        if scale_1_image == '' or scale_2_image == '' or scale_3_image == '':
            return False
        else:
            return True
    return False


# 文件是否已经
def exists_in_project(file_path):
    destination = os.path.basename(file_path)[0:-4] + '.png'
    for image in os.listdir(project_image_dir):
        if image == destination:
            return True
    return False


# 解析
def unzip(file_path):
    zip_obj = zipfile.ZipFile(file_path, 'r')
    destination = os.path.basename(file_path)[0:-4] + '.png'

    for name in zip_obj.namelist():
        if name.endswith('@3x.png'):
            target_path = os.path.join(project_image_dir, '3.0x', destination)
        elif name.endswith('@2x.png'):
            target_path = os.path.join(project_image_dir, '2.0x', destination)
        elif name.endswith('.png'):
            target_path = os.path.join(project_image_dir, destination)

        with zip_obj.open(name) as source, open(target_path, "wb") as target:
            shutil.copyfileobj(source, target)

    zip_obj.close()


# 生成代码
def generate_code(file_path):
    destination = os.path.basename(file_path)[0:-4]

    with open(project_code_file, "a") as file:
        file.write("\n  static const %s = Image_Root + \"%s.png\";" % (down_line_to_hump(destination), destination))


if __name__ == '__main__':
    print()
    for root, dirs, files in os.walk(download_dir):

        # 遍历找到正确的从蓝湖下载的iOS系统对应的zip文件
        for f in files:
            path = os.path.join(root, f)
            # 后缀是zip, zip文件名不包含中文, zip包含ios对应的三种规格图片文件, 项目中没有导入过这个图片
            if path.endswith('.zip') and not contain_chinese(f) and is_lanhu_zip(path) and not exists_in_project(path):
                # 解压zip到项目中指定的位置, 并使用zip文件名对图片进行重命名
                unzip(path)
                # 在项目中生成图片路径代码
                generate_code(path)

                print("成功导入 " + f)
