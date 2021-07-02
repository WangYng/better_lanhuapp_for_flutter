# better_lanhuapp_for_flutter
从蓝湖下载的图片快速导入到Flutter项目中, 并生成对应的代码

#### 主要代码
```python
# 遍历找到正确的从蓝湖下载的iOS系统对应的图片zip文件
for f in files:
    path = os.path.join(root, f)
    # 过滤条件: 后缀是zip, zip文件名不包含中文, zip包含ios对应的三种规格图片文件, 项目中没有导入过这个图片
    if path.endswith('.zip') and not contain_chinese(f) and is_lanhu_zip(path) and not exists_in_project(path):
        # 解压zip到项目中指定的位置, 并使用zip文件名对图片进行重命名
        unzip(path)
        # 在项目中生成图片路径代码
        generate_code(path)

        print("成功导入 " + f)

```
