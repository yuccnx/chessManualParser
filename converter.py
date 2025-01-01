#-*- coding: UTF-8 -*-

from xqfparser import *
from dpparser import *
from data import *

def reader_from_path(file_path):
    file_path = file_path.lower()
    if file_path.endswith(".xqf"):
        return XQFReader()
    elif file_path.endswith(".ubb"):
        return DPReader()

    return None

def writer_from_path(file_path):
    file_path = file_path.lower()
    if file_path.endswith(".xqf"):
        return XQFWriter()
    elif file_path.endswith(".ubb"):
        return DPWriter()

    return None

# 棋谱转换
def convert(path_src, path_des):

    qipu = QIPU()
    reader_from_path(path_src).read(path_src, qipu)
    print(qipu)
    writer_from_path(path_des).write(path_des, qipu)

    print(qipu.squares)

    print("from:%s to :%s finish!" % (path_src, path_des))
