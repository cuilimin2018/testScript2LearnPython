#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import sys
import os.path

def rename(dirname, oldname, newname):
	'''
	批量重命名目录内的文件，新名称为newname+number, number从1开始

	dirname: 目标目录名
	oldname: 文件原来的名称
	newname: 文件新名称
	'''
	#无论原dirname如何，统一成最后带目录分割符的形式
	if dirname[-1] != os.sep:
		dirname = dirname + os.sep

	if os.path.exists(dirname):
		oldnames=[]

		#列出dirname内文件名含有oldname的所有文件
		for old in os.listdir(dirname):
			if oldname in old:
				oldnames.append(old)
		index = 0

		#构建oldname和newname的绝对路径名，并重命名
		for index in range(len(oldnames)):
			ext = os.path.splitext(oldnames[index])[-1]
			old = os.path.join(dirname, oldnames[index])
			new = os.path.join(dirname, newname + str(index+1) + ext)
			os.rename(old, new)
	else:
		sys.exit(-1)

if __name__ == "__main__":
	rename(sys.argv[-3], sys.argv[-2], sys.argv[-1])
