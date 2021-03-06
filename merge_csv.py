

import pandas as pd
import os
Folder_Path = r"E:\movielens_data\csvFolder"  # 要拼接的文件夹及其完整路径，注意不要包含中文
SaveFile_Path = r"E:\movielens_data\data_process"  # 拼接后要保存的文件路径
SaveFile_Name = r'all.csv'  # 合并后要保存的文件名

# 修改当前工作目录
os.chdir(Folder_Path)
# 将该文件夹下的所有文件名存入一个列表
file_list = os.listdir()

# 读取第一个CSV文件并包含表头
# 编码默认UTF-8，若乱码自行更改
df = pd.read_csv(Folder_Path + '\\' + file_list[0], encoding='latin-1')

# 将读取的第一个CSV文件写入合并后的文件保存
df.to_csv(SaveFile_Path+'\\' + SaveFile_Name,
          encoding='latin-1', index=False)

# 循环遍历列表中各个CSV文件名，并追加到合并后的文件
for i in range(1, len(file_list)):
    df = pd.read_csv(Folder_Path + '\\' + file_list[i], encoding='latin-1')
    df.to_csv(SaveFile_Path+'\\' + SaveFile_Name,
              encoding='latin-1', index=False, header=False, mode='a+')
