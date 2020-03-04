 git 中 空目录不能提交，       在目录下 新建个  .gitkeep  空文件就行了， 
<!-- TOC -->

- [git工作流程](#git工作流程)
- [新建代码仓库](#新建代码仓库)
- [配置](#配置)
- [增删文件](#增删文件)
- [代码提交](#代码提交)
- [分支](#分支)
- [删除分支](#删除分支)
- [标签](#标签)
- [查看信息](#查看信息)
- [远程同步](#远程同步)
- [撤销](#撤销)
- [暂时将未提交的变化移除，稍后再移入](#暂时将未提交的变化移除稍后再移入)
- [其他](#其他)
- [git大规模文件更新](#git大规模文件更新)

<!-- /TOC -->

## git工作流程
		在工作目录中修改某些文件
		对修改后的文件进行快照，然后保存到暂存区域
		提交更新，将保存在暂存区域的
文件快照永久转储到Git目录中

## 新建代码仓库
		git init
			在当前目录新建一个Git代码库
		git init [project-name]
			子主题
		git clone [url]
			下载一个项目和它的整个代码历史

## 配置
		显示当前的Git配置
			git config --list
		编辑Git配置文件
			git config -e [--global]
		设置提交代码时的用户信
			git config [--global] user.name "[name]"
			git config [--global] user.email "[email address]"

## 增删文件
		git add
			git add [file1] [file2] ...
				添加指定文件到暂存区
			git add [dir]
				添加指定目录到暂存区，包括子目录
			git add .
				子主题
			git add -p
				添加每个变化前，都会要求确认
		git rm
			git rm [file1] [file2] ...
				删除工作区文件，并且将这次删除放入暂存区
			git rm --cached [file]
				停止追踪指定文件，但该文件会保留在工作区
		git mv [file-original] [file-renamed]
			改名文件，并且将这个改名放入暂存区

## 代码提交
		git commit -m [message]
			提交暂存区到仓库区
		git commit [file1] [file2] ... -m [message]
			提交暂存区的指定文件到仓库区
		git commit -a
			提交工作区自上次commit
之后的变化，直接到仓库区
		git commit -v
			提交时显示所有diff信息
		git commit --amend -m [message]
			使用一次新的commit，
替代上一次提交
		git commit --amend [file1] [file2] ...
			重做上一次commit，并包括指定文件的新变化

## 分支
		git branch
			列出所有本地分支
		git branch -r
			列出所有远程分支
		git branch -a
			列出所有本地分支和远程分支
		git branch [branch-name]
			新建一个分支，但依然停留在当前分支
		git checkout -b [branch]
			新建一个分支，并切换到该分支
		git branch [branch] [commit]
			新建一个分支，指向指定commit
		git branch --track [branch] [remote-branch]
			新建一个分支，与指定的远程分支建立追踪关系
		git checkout [branch-name]
			切换到指定分支，并更新工作区
		git checkout -
			切换到上一个分支
		git branch --set-upstream [branch] [remote-branch]
			建立追踪关系，在现有分支与指定的远程分支之间
		git merge [branch]
			合并指定分支到当前分支
		git cherry-pick [commit]
			选择一个commit，合并进当前分支
		git branch -d [branch-name]

## 删除分支
		删除远程分支
			git push origin --delete [branch-name]
			git branch -dr [remote/branch]

## 标签
		git tag
			列出所有tag
		git tag [tag]
			新建一个tag在当前commit
		git tag [tag] [commit]
			新建一个tag在指定commit
		git tag -d [tag]
			删除本地tag
		git push origin :refs/tags/[tagName]
			删除远程tag
		git show [tag]
			查看tag信息
		git push [remote] [tag]
			提交指定tag
		git push [remote] --tags
			提交所有tag
		git checkout -b [branch] [tag]
			新建一个分支，指向某个tag

## 查看信息
		git status
			显示有变更的文件
		git log
			显示当前分支的版本历史
		git log --stat
			显示commit历史，以及每次commit发生变更的文件
		git log -S [keyword]
			搜索提交历史，根据关键词
		git log [tag] HEAD --pretty=format:%s
			显示某个commit之后的所有变动，每个commit占据一行
		git log [tag] HEAD --grep feature
			显示某个commit之后的所有变化，其"提交说明"必须符合搜索条件
		显示某个文件的版本历史，包括文件改名
			git log --follow [file]
			git whatchanged [file]
		git log -p [file]
			显示指定文件相关的每一次diff
		git log -5 --pretty --oneline
			显示过去5次提交
		git shortlog -sn
			显示所有提交过的用户，按提交次数排序
		git blame [file]
			显示指定文件是什么人在什么时间修改过
		git diff
			显示暂存区和工作区的差异
		git diff --cached [file]
			显示暂存区和上一个commit的差异
		git diff HEAD
			显示工作区与当前分支最新commit之间的差异
		git diff [first-branch]...[second-branch]
			显示两次提交之间的差异
		git diff --shortstat "@{0 day ago}"
			显示今天你写了多少行代码
		git show [commit]
			显示某次提交的元数据和内容变化
		git show --name-only [commit]
			显示某次提交发生变化的文件
		git show [commit]:[filename]
			显示某次提交时，某个文件的内容
		git reflog
			显示当前分支的最近几次提交

## 远程同步
		git fetch [remote]
			下载远程仓库的所有变动
		git remote -v
			显示所有远程仓库
		git remote show [remote]
			显示某个远程仓库的信息
		git remote add [shortname] [url]
			增加一个新的远程仓库，并命名
		git pull [remote] [branch]
			取回远程仓库的变化，并与本地分支合并
		git push [remote] [branch]
			上传本地指定分支到远程仓库
		git push [remote] --force
			强行推送当前分支到远程仓库，即使有冲突
		git push [remote] --all
			推送所有分支到远程仓库

## 撤销
		git checkout [file
			恢复暂存区的指定文件到工作区
		git checkout [commit] [file]
			恢复某个commit的指定文件到暂存区和工作区
		git checkout .
			恢复暂存区的所有文件到工作区
		git reset [file]
			重置暂存区的指定文件，与上一次commit保持一致，但工作区不变
		git reset --hard
			重置暂存区与工作区，与上一次commit保持一致
		git reset [commit]
			重置当前分支的指针为指定commit，同时重置暂存区，但工作区不变
		git reset --hard [commit]
			重置当前分支的HEAD为指定commit，同时重置暂存区和工作区，与指定commit一致
		git reset --keep [commit]
			重置当前HEAD为指定commit，但保持暂存区和工作区不变
		git revert [commit]
			新建一个commit，用来撤销指定commit后者的所有变化都将被前者抵消，并且应用到当前分支

## 暂时将未提交的变化移除，稍后再移入
			git stash
			git stash pop

## 其他
		git archive
			生成一个可供发布的压缩包
		fetch和merge和pull的区别
			pull相当于git fetch 和 git merge的组合，
即更新远程仓库的代码到本地仓库，
然后将内容合并到当前分支
			git fetch：相当于是从远程获取
最新版本到本地，不会自动merge
			git merge : 将内容合并到当前分支
			git pull：相当于是从远程获
取最新版本并merge到本地
		git merge和git rebase的区别
			git merge branch会把branch分支的差
异内容pull到本地，然后与本地分支的内
容一并形成一个committer对象提交
到主分支上，合并后的分支与主分支一致；
			git rebase branch会把branch分支优先合并
到主分支，然后把本地分支的commit放到主分
支后面，合并后的分支就好像从合并后主分支又
拉了一个分支一样，本地分支本身不会保留提交历史
		HEAD、工作树和索引之间的区别
			HEAD文件包含当前分支的引用（指针）
			工作树是把当前分支检出到工作空间后形成的
目录树，一般的开发工作都会基于工作树进行
			索引index文件是对工作树进行代码修改后，
通过add命令更新索引文件；GIT系统通过
索引index文件生成tree对象
		git revert 和
git reset的区别
			git revert是用一次新的commit来回滚之前的
commit，此次提交之前的commit都会被保留
			git reset是回到某次提交，提交及之前的commit
都会被保留，此commit id之后的修改都会被删除
		配置不需要提交的文件
			利用命令touch .gitignore新建文件
			vim .gitignore//添加需要忽略哪些文件
夹下的什么类型的文件
		提交时发生冲突如何解决
			先在IDE里面对比本地文件和远程分支的文件；
然后把远程分支上文件的内容手工修改到本地文件；
然后再提交冲突的文件使其保证与远程分支的文件一致；
然后再提交自己修改的部分。
			通过git stash命令，把工作区的修改提交到栈区，目的是保存工作区的修改；
通过git pull命令，拉取远程分支上的代码并合并到本地分支，目的是消除冲突；
通过git stash pop命令，把保存在栈区的修改部分合并到最新的工作空间中；
		解释 Forking 工作流程的优点
			不是用单个服务端仓库充当“中央”代码库，
而是为每个开发者提供自己的服务端仓库；
因此Forking 工作流程常用于开源项目中
			主要优点是可以汇集提交贡献，又无需每个开发者提交到
一个中央仓库中，从而实现干净的项目历史记录。
			开发者先将提交推送到自己的公共仓库中；
然后向主仓库提交请求拉取（pull request）；
由项目维护人员集成更新
		Gitflow 工作流程
			Gitflow 工作流程使用两个并行的、
长期运行的分支来记录项目的历史记录，
分别是master和develop分支
			Master是准备发布线上版本的分支， 内
容是经过全面测试和核准的（生产就绪）
				Hotfix，维护（maintenance）
或修复（hotfix）分支是用于给快
速给生产版本修复打补丁的
			Develop是合并所有功能（feature）分支，
并执行所有测试的分支；当内容经过彻底检
查和修复后，才能合并到master分支
				Feature是具体功能开发的小分支

## git大规模文件更新

```
num=`git status |awk -F" "  '/add/{print NR}'`;echo $num   
for i in `git status |sed ' $num,$p'`;do git add $i;done    ## $num 代入之前的数字．

for i in `git status|grep "修改"|awk '{print $2}'`;do git add $i; done;
 for i in `git status|grep "新文件"|awk '{print $2}'`;do git add $i; done;
 for i in `git status|grep "删除"|awk '{print $2}'`;do git rm $i; done;
```