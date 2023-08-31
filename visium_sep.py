import numpy as np
import pandas as pd
import scanpy as sc
import os
import rpy2
from rpy2.robjects import r
import matplotlib
matplotlib.use('TkAgg')
from rpy2 import robjects
import matplotlib.pyplot as pl
from matplotlib import rcParams
import matplotlib.pyplot as plt

path=''

def up_dir(path):
    updir = os.path.abspath(os.path.join(path, "../"))
    updir = updir.replace('\\', '/')
    return updir

def show_figure(img_path):
    plt.figure(figsize=(7, 6))
    img = plt.imread(img_path)
    plt.imshow(img)
    plt.xticks([])  # 去掉x轴
    plt.yticks([])  # 去掉y轴
    plt.axis('off')  # 去掉坐标轴
    plt.show()

def get_png(p_p):
    img_path = sorted([os.path.join(p_p, name).replace('\\', '/') for name in os.listdir(p_p) if name.endswith('.png')])
    return img_path

def tran_1(path,min_cells,min_features,dims,resolution,point_size):
    f = open('visium/tran1.txt')

    data = f.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
    f.close()  # 关
    command = ''.join(data)
    command = command.replace('L7_callus1', path)
    command = command.replace('tran1',up_dir(path) + r'/visium_figure1')
    command = command.replace('min.cells = 10', 'min.cells = '+ min_cells )
    command = command.replace('min.features = 100', 'min.features = '+ min_features)
    command = command.replace('dims = 1:30', 'dims = 1:'+ dims)
    command = command.replace('resolution = 0.5', 'resolution = '+ resolution)
    command = command.replace('point_size = 3', 'point_size = '+ point_size)
    print(command)
    r(command)
    p_p = up_dir(path) + '/visium_figure1'
    img_path = get_png(p_p)
    for i in range(len(img_path)):
        show_figure(img_path[i])

def tran_2(path,point_size):
    f = open('visium/tran2.txt')

    data = f.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
    f.close()  # 关
    command = ''.join(data)
    command = command.replace('L7_callus1', path)
    command = command.replace('tran2',up_dir(path) + '/visium_figure2')
    command = command.replace('point_size = 3', 'point_size = ' + point_size)
    print(command)
    r(command)
    p_p = up_dir(path) + '/visium_figure2'
    img_path = get_png(p_p)
    for i in range(len(img_path)):
        show_figure(img_path[i])

def tran_3(path,point_size):
    f = open('visium/tran3.txt')

    data = f.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
    f.close()  # 关
    command = ''.join(data)
    command = command.replace('L7_callus1', path)
    command = command.replace('tran3',up_dir(path) + '/visium_figure3')
    command = command.replace('point_size = 2', 'point_size = ' + point_size)
    print(command)
    r(command)
    p_p = up_dir(path) + '/visium_figure3'
    img_path = get_png(p_p)
    for i in range(len(img_path)):
        show_figure(img_path[i])

def tran_4(path,point_size):
    f = open('visium/tran4.txt')

    data = f.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
    f.close()  # 关
    command = ''.join(data)
    command = command.replace('L7_callus1', path)
    command = command.replace('tran4',up_dir(path) + '/visium_figure4')
    command = command.replace('point_size = 2', 'point_size = ' + point_size)
    print(command)
    r(command)
    p_p = up_dir(path) + '/visium_figure4'
    img_path = get_png(p_p)
    for i in range(len(img_path)):
        show_figure(img_path[i])

def tran_5(path,point_size,top_gene,min_pct,logfc_threshold):
    f = open('visium/tran5.txt')

    data = f.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
    f.close()  # 关
    command = ''.join(data)
    command = command.replace('L7_callus1', path)
    command = command.replace('tran5',up_dir(path) + '/visium_figure5')
    command = command.replace('point_size = 2', 'point_size = ' + point_size)
    command = command.replace('top_gene = 1', 'top_gene = ' + top_gene)
    command = command.replace('min.pct = 0.25', 'min.pct = ' + min_pct)
    command = command.replace('logfc.threshold = 0.25', 'logfc.threshold = ' + logfc_threshold)
    print(command)
    r(command)
    p_p = up_dir(path) + '/visium_figure5'
    img_path = get_png(p_p)
    for i in range(len(img_path)):
        show_figure(img_path[i])

def tran_6(path,point_size,gene_list):
    f = open('visium/tran6.txt')

    data = f.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
    f.close()  # 关
    command = ''.join(data)
    command = command.replace('L7_callus1', path)
    command = command.replace('tran6',up_dir(path) + '/visium_figure6')
    command = command.replace('point_size = 2.6', 'point_size = ' + point_size)
    command = command.replace("gene_list = c('Solyc07g007755.2')", "gene_list = c(" + gene_list + ")")
    print(command)
    r(command)
    p_p = up_dir(path) + '/visium_figure6'
    img_path = get_png(p_p)
    for i in range(len(img_path)):
        show_figure(img_path[i])

def tran_7(path,point_size):
    f = open('visium/tran7.txt')

    data = f.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
    f.close()  # 关
    command = ''.join(data)
    command = command.replace('L7_callus1', path)
    command = command.replace('tran7',up_dir(path) + '/visium_figure7')
    command = command.replace('point_size = 2', 'point_size = ' + point_size)
    print(command)
    r(command)
    p_p = up_dir(path) + '/visium_figure7'
    img_path = get_png(p_p)
    for i in range(len(img_path)):
        show_figure(img_path[i])


#rpy2.robjects.r('plot(t)')

#t2=rpy2.robjects.r('plot(t)')
#print(t2)


