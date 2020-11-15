#!/usr/bin python3
import shutil
import os

ckPath = "/media/Data/CK+/CK+/cohn-kanade-images"

ckCopyPath = "/home/szmurlh/CK+_Copy"
for root, dirs, files in os.walk(ckPath):
    for dr in dirs:
        if isdir(dr):
            for f in listdir(dr):
                shutil.move(dr+"/"+f, up +"/"+f)




