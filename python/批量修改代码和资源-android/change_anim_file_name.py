#!/usr/bin/env python
#coding:utf-8

import os
import os.path
import io
import utils
manifest = utils.manifest
rootCodeDir = utils.rootCodeDir
rootResDir = utils.rootResDir

print("start")

# 获取所有的布局文件，并修改文件名
changedNames = {}
def refactorFileNames(directory):
	list = os.listdir(directory)
	for i in range(0, len(list)):
		fileName = list[i]
		newFileName = utils.addPrefix(fileName)
		if (len(newFileName) > 0):
			# 重命名文件
			os.rename(directory + os.path.sep + fileName, directory + os.path.sep + newFileName)
			# 保存到map
			if fileName.find('.') > 0:
				changedNames[fileName[0:fileName.find('.')]] = newFileName[0:newFileName.find('.')]
			else:
				changedNames[fileName] = newFileName

# 修改文件内容
def changeContent(fileContent):
	# import kotlinx.android.synthetic.main.wbu_activity_friend_splash_match.*
	for fileName in changedNames:
		if fileContent.find(fileName) >= 0:
			if fileContent.find("anim/" + fileName + "<") >= 0:
				fileContent = fileContent.replace("anim/" + fileName  + "<", "anim/" + changedNames[fileName] + "<")
			if fileContent.find("anim." + fileName) >= 0:
				fileContent = fileContent.replace("anim." + fileName, "anim." + changedNames[fileName])
	return fileContent

# 修改目录下所有的文件，并遍历子目录
def changeDirContent(dir):
	list = os.listdir(dir)
	for i in range(0, len(list)):
		filePath = dir + os.path.sep + list[i]
		if os.path.isfile(filePath):
		    if filePath.endswith(".xml") or filePath.endswith(".java") or filePath.endswith(".kt"):
				fileContent = ""
				with io.open(filePath, "r", encoding="utf-8") as file:
				    fileContent = changeContent(file.read())
				with io.open(filePath, "w", encoding="utf-8") as file:
				    file.write(fileContent)
		else:
			changeDirContent(filePath)




# 并修改文件名
refactorFileNames(rootResDir + os.path.sep + "anim")
# 遍历代码文件，修改变量
changeDirContent(rootCodeDir)
changeDirContent(rootResDir)

manifestContent = ""
with io.open(manifest, "r", encoding="utf-8") as file:
	manifestContent = file.read()
manifestContent = changeContent(manifestContent)
with io.open(manifest, "w", encoding="utf-8") as file:
	file.write(manifestContent)

print("finished")