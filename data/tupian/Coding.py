import os
from PIL import Image

path = 'E:/google download/HAN-master/src/dataset/original/Set5/x4'  # 原始图片位置
newpath = 'E:/google download/HAN-master/src/dataset/coded/urban100'  # 保存图片位置
c = 0  # 从0开始
filelists = os.listdir(path)
for line in filelists:
    img = Image.open(path + '/' + line)

    a = "0" * (6 - len(str(c)))  # 6 是命名的位数,可以修改
    out = a + str(c) + '_' + 'LR' '.png'
    img.save(out, path=newpath)
    c += 1
