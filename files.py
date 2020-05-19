# -*- coding: <UTF-8> -*-
import os

def dif(d1,d2):
    f1 = os.listdir(path=d1)
    f2 = os.listdir(path=d2)
    for i in range(len(f1)):
        if f1[i] not in f2:
            print(f1[i])
dif(r"first_dir",r"second_dir")#какие файлы есть только в первой директории