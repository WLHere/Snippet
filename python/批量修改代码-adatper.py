#!/usr/bin/env python3

import os
import os.path
rootCodeDir = os.path.abspath(os.getcwd() +  "/../src/main/java")

print("rootCodeDir = " + rootCodeDir)

def replaceCodes(fileContent):
	imports = {
		"import com.*.*.R": "import com.*.*.R",
		
	}
	contents = {
		"*****": "*******",
		
	}
	for key in imports:
		if (fileContent.find(key) >= 0):
			fileContent = fileContent.replace(key, imports[key])

	for key in contents:
		if (fileContent.find(key) >= 0):
			fileContent = fileContent.replace(key, contents[key])
	return fileContent


# 修改代码文件
def adpatCodeFile(filePath):
	fileContent = ""
	# if (filePath.find("com" + os.path.sep + "*" + os.path.sep + "*") >= 0):
	# 	return

	with open(filePath, "r") as file:
		fileContent = file.read()

	fileContent = replaceCodes(fileContent)

	with open(filePath, "w") as file:
			file.write(fileContent)

# 遍历代码文件
def loopSourceFiles(dir):
	list = os.listdir(dir)
	for i in range(0, len(list)):
		path = dir + os.path.sep + list[i]
		if os.path.isfile(path):
			adpatCodeFile(path)
		else:
			loopSourceFiles(path)

loopSourceFiles(rootCodeDir)

