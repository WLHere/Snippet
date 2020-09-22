#!/usr/bin/env python
#coding:utf-8

import os
import os.path
rootCodeDir = os.path.abspath(os.getcwd() +  "/../src")
rootLayoutDir = os.path.abspath(os.getcwd() +  "/../res/layout")

print("rootCodeDir = " + rootCodeDir)

def replaceCodes(fileContent):
	imports = {
		"import ***.R": "import  ***..R",
		
	}
	contents = {
		" ***": " ***",
		
	}
	for key in imports:
		if (fileContent.find(key) >= 0):
			fileContent = fileContent.replace(key, imports[key])

	for key in contents:
		if (fileContent.find(key) >= 0):
			fileContent = fileContent.replace(key, contents[key])
	return fileContent


def replaceLayout(fileContent):
	contents = {
		"***": "***",
	}

	for key in contents:
		if (fileContent.find(key) >= 0):
			fileContent = fileContent.replace(key, contents[key])
	return fileContent


# 修改代码文件
def adpatCodeFile(filePath):
	fileContent = ""
	if (filePath.find("com" + os.path.sep + "wuba" + os.path.sep + "jiaoyou") >= 0):
		return

	with open(filePath, "r") as file:
		fileContent = file.read()

	fileContent = replaceCodes(fileContent)

	with open(filePath, "w") as file:
			file.write(fileContent)

# 修改代码文件
def adpatLayoutFile(filePath):
	fileContent = ""
	if (filePath.find("com" + os.path.sep + "wuba" + os.path.sep + "jiaoyou") >= 0):
		return

	with open(filePath, "r") as file:
		fileContent = file.read()

	fileContent = replaceLayout(fileContent)

	with open(filePath, "w") as file:
			file.write(fileContent)

# 遍历代码文件
def loopCodeFiles(dir):
	list = os.listdir(dir)
	for i in range(0, len(list)):
		path = dir + os.path.sep + list[i]
		if os.path.isfile(path):
			adpatCodeFile(path)
		else:
			loopCodeFiles(path)


# 遍历布局文件
def loopLayoutFiles(dir):
	list = os.listdir(dir)
	for i in range(0, len(list)):
		path = dir + os.path.sep + list[i]
		if os.path.isfile(path):
			adpatLayoutFile(path)
		else:
			loopLayoutFiles(path)

loopCodeFiles(rootCodeDir)
loopLayoutFiles(rootLayoutDir)

