# -*-coding:utf-8-*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#函数1，读取TXT文件，参数一：文件名，参数二：分隔方式
def readXYZfile(filename, Separator):
    data = [[], [], []]
    f = open(filename, 'r')
    line = f.readline()

    num = 0
    while line:  # 按行读入点云
        k =line.split(Separator)
        data[0].append(k[0])  # X坐标
        data[1].append(k[1])  # Y坐标
        data[2].append(k[2])  # Z坐标
        num = num + 1
        line = f.readline()
    f.close()

    # string型转float型
    x = [float(data[0]) for data[0] in data[0]]
    z = [float(data[1]) for data[1] in data[1]]
    y = [float(data[2]) for data[2] in data[2]]
    print("读入点的个数为:{}个。".format(num))
    point = [x, y, z]
    return point


# 三维离散点图显示点云
def displayPoint(data, title):
    # 散点图参数设置
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_title(title)
    ax.scatter3D(data[0], data[1], data[2], c='r', marker='.')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()

if __name__ == "__main__":
    data = readXYZfile("dawye_ex.txt", '\t')
    displayPoint(data, "TREE_DAWANGYE")