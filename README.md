# better_lanhuapp_for_flutter
从蓝湖下载的图片快速导入到Flutter项目中, 并生成对应的代码

## 处理流程
1. 遍历找到正确的从蓝湖下载的iOS系统对应的图片zip文件
2. 过滤条件: 后缀是zip, zip文件名不包含中文, zip包含ios对应的三种规格图片文件
3. 解压zip到项目中指定的位置, 并使用zip文件名对图片进行重命名
4. 在项目中生成图片路径代码

## 用法
1. 在项目根目录生成 env.py
```python
# 从蓝湖下载的图片目录
download_dir = '/Users/xxx/Downloads'

# flutter项目图片目录
project_image_dir = '/Users/xxx/static/images'

# flutter项目图片路径代码文件
project_code_file = '/Users/xxx/lib/config/image_path.dart'

# 如果项目中已经导入了同名文件是否强制覆盖
isForceCover = True
```
2. 运行main.py