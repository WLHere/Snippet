#!/usr/bin/env python
#coding:utf-8

import os
import os.path
import io
# from xml.dom.minidom import parse
import xml.dom.minidom
import utils

manifest = utils.manifest
rootCodeDir = utils.rootCodeDir
rootResDir = utils.rootResDir

print("start")
changedNames = {}
changedNames["string"] = {}
changedNames["dimen"] = {}
changedNames["color"] = {}
changedNames["string-array"] = {}
changedNames["style"] = {}
changedNames["drawable"] = {}

typeNames = {}
typeNames["string"] = "string"
typeNames["dimen"] = "dimen"
typeNames["color"] = "color"
typeNames["string-array"] = "array"
typeNames["style"] = "style"
typeNames["drawable"] = "drawable"


valueFiles = []
# 找到所有的values文件
resDirs = os.listdir(rootResDir)
for i in range(0, len(resDirs)):
	if resDirs[i].startswith("values") and os.path.isdir(rootResDir + os.path.sep + resDirs[i]):
		valueDir = rootResDir + os.path.sep + resDirs[i]
		subFileNames = os.listdir(valueDir)
		for j in range(0, len(subFileNames)):
			filePath = valueDir + os.path.sep + subFileNames[j]
			if os.path.isfile(filePath) and filePath.endswith(".xml"):
				valueFiles.append(filePath)

# 更改所有的values文件
for i in range(0, len(valueFiles)):
	valueFile = valueFiles[i]
	
	DOMTree = xml.dom.minidom.parse(valueFile)
	collection = DOMTree.documentElement
	changed = False
	for key in changedNames:
		values = collection.getElementsByTagName(key)
		for value in values:
			name = value.getAttribute("name")
			prefixedName = utils.addPrefix(name)
			if (len(prefixedName) > 0):
				changed = True
				changedNames[key][name] = prefixedName
				value.setAttribute("name", prefixedName)
	if changed:
		xmlContent = DOMTree.toxml()
		xmlContent = xmlContent.replace("<?xml version=\"1.0\" ?><resources>", "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<resources>")
		with io.open(valueFile, "w", encoding="utf-8") as file:
			file.write(xmlContent)


# 修改文件内容
def changeContent(fileContent, valueType, values):
	typeName = typeNames[valueType]
	for value in values:
		if fileContent.find(value) >= 0:
			if fileContent.find(typeName + "/" + value + "\"") >= 0:
				fileContent = fileContent.replace(typeName + "/" + value + "\"", typeName + "/" + values[value] + "\"")
			if fileContent.find(typeName + "/" + value + "<") >= 0:
				fileContent = fileContent.replace(typeName + "/" + value + "<", typeName + "/" + values[value] + "<")
			if fileContent.find("parent=\"" + value + "\"") >= 0:
				fileContent = fileContent.replace("parent=\"" + value + "\"", "parent=\"" + values[value] + "\"")
			if fileContent.find(typeName + "." + value) >= 0:
				fileContent = fileContent.replace(typeName + "." + value, typeName + "." + values[value])
	return fileContent

def changeFileContent(filePath):
	if (filePath.endswith(".xml") or filePath.endswith(".java") or filePath.endswith(".kt")):
		with io.open(filePath, "r", encoding="utf-8") as file:
			fileContent = file.read()
			for valueType in changedNames:
				fileContent = changeContent(fileContent, valueType, changedNames[valueType])
		with io.open(filePath, "w", encoding="utf-8") as file:
			file.write(fileContent)

# 修改目录下所有的文件，并遍历子目录
def changeDirContent(dir):
	list = os.listdir(dir)
	for i in range(0, len(list)):
		filePath = dir + os.path.sep + list[i]
		if os.path.isfile(filePath):
			changeFileContent(filePath)
		else:
			changeDirContent(filePath)

changeDirContent(rootCodeDir)
changeDirContent(rootResDir)
changeFileContent(manifest)

print("finished")