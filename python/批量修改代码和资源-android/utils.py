#coding:utf-8
import os

def addPrefix(name):
	# 添加wbu_jy_前缀
	prefixedName = ""
	if (name.startswith("wbu_jy_") or name.startswith(".")):
		return prefixedName
	elif (name.startswith("wbu_town_")):
		prefixedName = "wbu_jy_" + name[9:]
	elif (name.startswith("wbu_")):
		prefixedName = "wbu_jy_" + name[4:]
	else:
		prefixedName = "wbu_jy_" + name
	return prefixedName

manifest = os.path.abspath(os.getcwd() +  "/../AndroidManifest.xml")
rootCodeDir = os.path.abspath(os.getcwd() +  "/../src")
rootResDir = os.path.abspath(os.getcwd() +  "/../res/")