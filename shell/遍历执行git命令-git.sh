#! /bin/sh

# 提取命令
cmd=$*
# 删除命令中的"git"字符
cmd=${cmd#git}
# 判断命令是否为空
if [ ! "$cmd" ]; then
    echo "please input cmd as \"branch or git branch\""
    exit
fi
# 添加git前缀
cmd="git ${cmd}"

if [ -d "../.git" ]; then
	cd ..
fi
echo "当前目录"
pwd

# 提取git子目录
# 定义数组
declare -a repoDirs
index=0

# 获取子目录
files=$(ls -d */)
for file in $files
do
    if [ -d "${file}/.git" ]; then
        # 包含.git目录，是git库
        repoDirs[$index]=$file
        index=$(($index+1))
    fi
done

line="-------------------------------------------------"

# 在当前目录执行命令
echo $line
echo "Root Project"
eval $cmd

# 遍历子目录，执行命令
for repoDir in ${repoDirs[@]}
do
    echo $line
    echo $repoDir
    eval "cd ${repoDir}"
    eval $cmd
    eval "cd .."
done
echo $line
