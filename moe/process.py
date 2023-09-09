import os
import json


# 定义生成JSON的函数
def generate_json(root_dir):
    result = {}

    for dir_name, subdirs, files in os.walk(root_dir):
        # 一级目录名称
        top_dir_name = os.path.basename(dir_name)

        # 仅处理图片文件
        image_files = [
            f
            for f in files
            if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"))
        ]

        if image_files:
            container = []
            for image_file in image_files:
                # 构造图片路径
                image_path = (
                    os.path.join(dir_name, image_file)
                    .replace("\\", "/")
                    .replace("./", "")
                )
                # 构造图标的HTML
                icon_html = f'<img src="https://cdn.casecori.top/gh/cystee/om/moe/{image_path}">'
                # 添加到container
                container.append({"icon": icon_html, "text": image_file})

            # 添加到结果中
            result[top_dir_name] = {"type": "image", "container": container}

    return result


# 设置根目录
root_directory = "./"

# 生成JSON数据
json_data = generate_json(root_directory)

# 将数据写入JSON文件
with open("output.json", "w", encoding="utf-8") as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=4)

print("JSON文件已生成：output.json")
