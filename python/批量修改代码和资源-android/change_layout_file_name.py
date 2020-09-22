#!/usr/bin/env python
#coding:utf-8

import os
import os.path
import io
import utils
manifest = utils.manifest
rootCodeDir = utils.rootCodeDir
rootResDir = utils.rootResDir
rootLayoutDir = rootResDir + os.path.sep + "layout"

print("start")


# 获取所有的布局文件，并修改文件名
layoutNames = {}
def refactorLayoutNames():
	layoutDir = rootLayoutDir
	list = os.listdir(rootLayoutDir)
	for i in range(0, len(list)):
		layoutName = list[i]
		newLayoutName = utils.addPrefix(layoutName)
		if (len(newLayoutName) > 0):
			# 重命名文件
			os.rename(layoutDir + os.path.sep + layoutName, layoutDir + os.path.sep + newLayoutName)
			# 保存到map
			if layoutName.find('.') > 0:
				layoutNames[layoutName[0:layoutName.find('.')]] = newLayoutName[0:newLayoutName.find('.')]
    		else:
				layoutNames[layoutName] = newLayoutName

# 修改文件内容
def changeContent(fileContent):
	# import kotlinx.android.synthetic.main.wbu_activity_friend_splash_match.*
	for layoutName in layoutNames:
		if fileContent.find(layoutName) >= 0:
			if fileContent.find("layout/" + layoutName) >= 0:
				fileContent = fileContent.replace("layout/" + layoutName, "layout/" + layoutNames[layoutName])
			if fileContent.find("layout." + layoutName) >= 0:
				fileContent = fileContent.replace("layout." + layoutName, "layout." + layoutNames[layoutName])
			if fileContent.find("kotlinx.android.synthetic.main." + layoutName) >= 0:
				fileContent = fileContent.replace("kotlinx.android.synthetic.main." + layoutName, "kotlinx.android.synthetic.main." + layoutNames[layoutName])
	return fileContent

# 修改目录下所有的文件，并遍历子目录
def changeDirContent(dir):
	list = os.listdir(dir)
	for i in range(0, len(list)):
		filePath = dir + os.path.sep + list[i]
		if os.path.isfile(filePath):
		    if (filePath.endswith(".xml") or filePath.endswith(".java") or filePath.endswith(".kt")):
				fileContent = ""
				with io.open(filePath, "r", encoding="utf-8") as file:
				    fileContent = changeContent(file.read())
				with io.open(filePath, "w", encoding="utf-8") as file:
				    file.write(fileContent)
		else:
			changeDirContent(filePath)



# 获取所有的布局文件，并修改文件名
refactorLayoutNames()
# 遍历代码文件，修改layout变量
changeDirContent(rootCodeDir)
# 遍历布局文件，修改layout变量
changeDirContent(rootLayoutDir)

print("finished")