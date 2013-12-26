#! /usr/local/bin/python3.3m
# -*- coding: utf-8 -*-

#-------------------
# author: Hero Peng
# date: 2013/12/15
# version: 1.0.0
#-------------------
"""这个脚本用来复制指定格式的文件到指定的文件夹中"""
import os
import shutil
 
os.chdir ('/Users/heropeng/Downloads/')  # 这里默认的下载文件夹
cwd = os.getcwd()
for path, dirnames, filenames in os.walk(cwd):
	for filename in filenames:
		(fname, ftail) = os.path.splitext (filename)
		if ftail == ".pdf":
			shutil.copy(filename, "/Users/heropeng/Documents/books/")  # 将指定格式的文件复制到指定文件夹

