import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd #打开excel文件
import xlwt
excelfile = r"kmeans.xlsx"  # excel文件地址
wb = xlrd.open_workbook(filename=excelfile)
sheet1=wb.sheet_by_index(0)
df = pd.read_excel(excelfile)  # 读取excel文件,默认表单1
# print("获取到所有数据:\n{0}".format(df))#打印excel文件内容，用于检错
data = df.iloc[:, 1:].values  # 读所有行的属性列的值
# print(data)#打印属性数据内容，用于检错
#row = len(data)  # 属性数据行数
row=len(data)
col = len(data[0])  # 属性数据列数
n = input("请输入n的值： ")
randomNum = random.sample(range(0, row), int(n))  # n个随机数


def dist_eclud(vecA, vecB):  # 计算两个向量之间的欧氏距离
    vec_square = []
    for i in vecA - vecB:
        i = i ** 2
        vec_square.append(i)
    return sum(vec_square) ** 0.5


re = []  # 结果簇列表
temp = []
num = []

for i in randomNum:
    re.append(data[i])
    temp.append(data[i])
    num.append(0)


def euclid_Distance(A, B):  # 求两行数据间的欧式距离
    t = 0
    for i in range(len(A)):
        t += np.square(A[i] - B[i])
    return np.sqrt(t)


def is_Same(A, B):  # 判断两list数据是否相等
    bl = True
    for i1 in range(len(A)):
        for i2 in range(len(A[0])):
            if A[i1][i2] != B[i1][i2]:
                bl = False
                break
        if bl == False:
            break
    return bl


def init(A):  # 数据初始化为0
    if isinstance(A[0], int):
        A = [0] * len(A)
    else:
        A = [[0] * len(A[0]) for row in range(len(A))]
    return A


while True:
    temp = init(temp)
    num = init(num)
    for i1 in range(len(data)):
        tit = -1
        t = 0x3f3f3f3f
        for i2 in range(len(re)):
            tt = euclid_Distance(data[i1], re[i2])
            if t > tt:
                t = tt
                tit = i2
        for i3 in range(len(data[0])):
            temp[tit][i3] += data[i1][i3]
        num[tit] += 1
    for i4 in range(len(temp)):
        for i5 in range(len(temp[0])):
            temp[i4][i5] /= num[i4]
    if is_Same(re, temp):
        print(re)
        if len(data[0]) == 2:
            _color = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
            for i6 in range(len(data)):
                tit = -1
                t = 0x3f3f3f3f
                for i7 in range(len(re)):
                    tt = euclid_Distance(data[i6], re[i7])
                    if t > tt:
                        t = tt
                        tit = i7
                plt.scatter(data[i6][0], data[i6][1], c=_color[tit])
            plt.show()
        break
    re = temp