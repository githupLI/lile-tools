#!/usr/bin/python
  2 # -*- coding:utf-8 -*-
  3 import os
  4 import sys
  5 def rename():
  6     #path='/home/security/zt/db/db'
  7     path=input("请输入文件夹路径:")
  8     name=input("请输入开头名:")
  9     startNumber=input("请输入开始数:")
 10     fileType=input("请输入后缀名（如 .jpg、.txt等等）:")
 11     print("正在生成以"+name+startNumber+fileType+"迭代的文件名")
 12     count=0
 13     filelist=os.listdir(path)
 14     for files in filelist:
 15         Olddir=os.path.join(path,files)
 16         if os.path.isdir(Olddir):
 17             continue
 18         Newdir=os.path.join(path,name+str(count+int(startNumber))+fileType)
 19         os.rename(Olddir,Newdir)
 20         count+=1
 21     print("一共修改了"+str(count)+"个文件")
 22 rename()
