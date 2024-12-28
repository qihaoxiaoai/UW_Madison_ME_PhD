import os
import img2pdf
from tqdm import tqdm

def jpg_to_pdf(directory, output_filename):
    # 收集目录下的所有 JPG 文件，并按文件名中的数字部分排序
    jpg_files = sorted(
        [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.jpg') and file.startswith('page_')],
        key=lambda x: int(x.split('_')[1].split('.')[0])  # 提取数字部分并转换为整数
    )
    
    # 检查是否有文件被加载
    if not jpg_files:
        print("No jpg files found in the directory.")
        return
    
    print("Creating PDF file...")
    # 将图片转换为 PDF
    with open(output_filename, 'wb') as file:
        file.write(img2pdf.convert(jpg_files))

    # 使用 tqdm 显示进度
    for i in tqdm(range(len(jpg_files)), desc="Processing images"):
        pass  # tqdm 进度更新
    
    print(f"PDF file created: {output_filename}")

# 调用函数，假设所有图片都在当前目录下
jpg_to_pdf('.', 'output.pdf')

