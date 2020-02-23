<!-- TOC -->

- [ssh  远程运行命令](#ssh--远程运行命令)
- [getopts 与 getopt ，shell 脚本 接收 外界参数](#getopts-与-getopt-shell-脚本-接收-外界参数)
- [awk 获取变量](#awk-获取变量)
- [shell 脚本技巧 ,健壮性](#shell-脚本技巧-健壮性)

<!-- /TOC -->

## ssh  远程运行命令
pssh
		https://blog.csdn.net/fdipzone/article/details/23000201
		 #!/bin/bash

ssh -f -n -l www-online 192.168.110.34 "/home/www-online/uptimelog.sh &" # 后台运行ssh

pid=$(ps aux | grep "ssh -f -n -l www-online 192.168.110.34 /home/www-online/uptimelog.sh" | awk '{print $2}' | sort -n | head -n 1) # 获取进程号

echo "ssh command is running, pid:${pid}"

sleep 3 && kill ${pid} && echo "ssh command is complete" # 延迟3秒后执行kill命令，关闭ssh进程，延迟时间可以根据调用的命令不同调整

exit 0

————————————————

版权声明：本文为CSDN博主「傲雪星枫」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。

原文链接：https://blog.csdn.net/fdipzone/article/details/23000201

## getopts 与 getopt ，shell 脚本 接收 外界参数
		https://cloud.tencent.com/developer/article/1043821

## awk 获取变量
```
work_pwd="/cloud/app/sls-common/WebServer#/sls_web/1207787_sls-common_WebServer"


## 基础样式
sudo cat > ./overwrite.sh << EOF

#!/bin/sh
work_dir=/cloud/app/sls-backend-server/InitDependentSystem#/init_dependent_system

ls \$work_dir/1350852_sls-backend-server_InitDependentSystem
sudo mkdir \$work_dir/1350852_sls-backend-server_InitDependentSystem.overwrite
sudo /cloud/tool/tianji/overwrite add sls-backend-server InitDependentSystem# init_dependent_system 1350852_sls-backend-server_InitDependentSystem 30 -f  ## 添加 overwrite
sudo cp -pr \$work_dir/1350852_sls-backend-server_InitDependentSystem/* \$work_dir/1350852_sls-backend-server_InitDependentSystem.overwrite/
# sudo /cloud/tool/tianji/overwrite remove sls-backend-server InitDependentSystem# init_dependent_system 1350852_sls-backend-server_InitDependentSystem   ## 移除 overwrite
# sudo rm -rf /cloud/app/sls-backend-server/InitDependentSystem#/init_dependent_system/1350852_sls-backend-server_InitDependentSystem.overwrite

sudo tjc stop sls-backend-server.InitDependentSystem#
sudo tjc start sls-backend-server.InitDependentSystem#
EOF

## 修改参数
eval $(echo $work_pwd|awk -F"/cloud/app" '{print $2}'|awk -F"/" '{printf("Service=%s;SR=%s;APP=%s;BuildID=%s;",$2,$3,$4,$5)}')

sudo sed -i "s/1350852_sls-backend-server_InitDependentSystem/$BuildID/g" ./overwrite.sh                             # 修改 buildID 
sudo sed -i "s/sls-backend-server/$Service/g" ./overwrite.sh             # 修改 service
sudo sed -i "s/InitDependentSystem#/$SR/g" ./overwrite.sh             # 修改 SR
sudo sed -i "s/init_dependent_system/$APP/g" ./overwrite.sh  # 修改 application
```

## shell 脚本技巧 ,健壮性
		https://zhuanlan.zhihu.com/p/73728157
		 https://twosee.cn/2018/03/18/stronger-shell/#%E4%BD%BF%E7%94%A8set-u
		 https://segmentfault.com/a/1190000006900083
		 https://segmentfault.com/a/1190000002539169
		 https://zhuanlan.zhihu.com/p/46100771
		 https://stackoverflow.com/questions/35800082/how-to-trap-err-when-using-set-e-in-bash
	 例子
		
```
#!/bin/bash

set -e -o errtrace -o pipefail  ## set -eE / set -e -o errtrace  检测到 程序出错后，报错，中断。 
err() {
    echo "Error occurred:"
    awk 'NR>L-3 && NR<L+3 { printf "%-5d%3s%s\n",NR,(NR==L?">>>":""),$0 }' L=$1 $0
}
## 用来捕获  异常的 信号， ，捕获到之后， 执行上面的 err() {} 函数
trap 'err $LINENO' ERR

## 用来捕获异常的  函数。
function error_exit {
  echo "$1" 1>&2
  exit 1
}


ARGS=`getopt -o h:: --long "src_files:,dest_dir:,remove::" -n 'example.sh' -- "$@"`
if [ $? != 0 ]; then
    ## echo -e '\n'  换行
    echo -e "EROOR, the ADD overwrite option is:  bash overwrite.sh --src_files=XXX --dest_dir=XX \n or the REMOVE overwrite  option is:  bash overwrite.sh --dest_dir=XX --remove"
    exit 1
fi


#echo $ARGS ，  getopt, 还有一种 getopts
#将规范化后的命令行参数分配至位置参数（$1,$2,...)
eval set -- "${ARGS}"

while true
do
    case "$1" in
        -h)
            echo -e "the ADD overwrite option is:  bash overwrite.sh --src_files=XXX --dest_dir=XX \n or the REMOVE overwrite  option is:  bash overwrite.sh --dest_dir=XX --remove"
            echo "--src_files is divided by ','"
            echo "--dest_dir is like '/cloud/app/sls-common/WebServer#/sls_web/current', it must start with '/cloud/app/sls-common/WebServer#/sls_web/' "
            echo "--remove ,when you want to remove overwrite"
            shift
            ;;
        --src_files)
            echo "--src_files is $2";
            source_files_str=`echo $2 |sed 's/,/ /g'`;  ## 将 逗号 转为空格
            read -a source_files_list  <<< $source_files_str;  ## 将 str 转为数组， 以 单个或多个 空格为分隔。
            for source_file in ${source_files_list[*]}
            do
                ## “||” error_exit  捕获异常， “||”之前的的语句 执行失败，就会 执行 后面的。
                [[ -e $source_file ]] || error_exit "$source_file no exist"
            done
            shift 2
            ;;
        --dest_dir)
            echo $2 | grep ^/cloud/app/ > /dev/null 2>&1 || error_exit "--dest_dir must start with '/cloud/app/'"
            echo "--dest_dir is $2"
            dest_dir=$2
            shift 2
            ;;
        --remove)
            echo "remove overwrite"
            scripts_option="remove"
            shift 2
            ;;
        --)
            shift
            break
            ;;
        *)
            echo -e "EROOR, the ADD overwrite option is:  bash overwrite.sh --src_files=XXX --dest_dir=XX \n or the REMOVE overwrite  option is:  bash overwrite.sh --dest_dir=XX --remove"
            echo "Internal error!"
            exit 1
            ;;
    esac
done

#处理剩余的参数
for arg in $@
do
    echo "processing $arg"
done

write_overwrite_sh () {
## \$current_dir 在 cat 添加的时候 转义。
sudo cat > ./overwrite.sh << EOF
#!/bin/sh
current_dir=/cloud/app/sls-backend-server/InitDependentSystem#/init_dependent_system

sudo mkdir  -p \$current_dir/1350852_sls-backend-server_InitDependentSystem.overwrite
sudo /cloud/tool/tianji/overwrite add sls-backend-server InitDependentSystem# init_dependent_system 1350852_sls-backend-server_InitDependentSystem 30 -f  
sudo cp -pr \$current_dir/1350852_sls-backend-server_InitDependentSystem/* \$current_dir/1350852_sls-backend-server_InitDependentSystem.overwrite/
##### sudo /cloud/tool/tianji/overwrite remove sls-backend-server InitDependentSystem# init_dependent_system 1350852_sls-backend-server_InitDependentSystem   
##### sudo rm -rf /cloud/app/sls-backend-server/InitDependentSystem#/init_dependent_system/1350852_sls-backend-server_InitDependentSystem.overwrite

# echo '### restart SR '
sudo tjc stop sls-backend-server.InitDependentSystem# > /dev/null 2>&1 && sudo tjc start sls-backend-server.InitDependentSystem#  > /dev/null 2>&1;
EOF
}

get_common_varabiles () {
    ## 获取变量  ## 按'/' 分隔后 设置变量。 Service=$2 ;SR=$3 ;APP=$4;
    eval $(echo $dest_dir|awk -F"/cloud/app" '{print $2}'|awk -F"/" '{printf("Service=%s;SR=%s;APP=%s;",$2,$3,$4)}')
    current_dir=`echo $dest_dir|awk -F'current' '{print $1}'`
    alread_install_dir=$current_dir'current/alread_installed'
    overwrite_script=$current_dir'overwrite.sh'

    machine_ip_str=`tj_show -ip -r $Service'.'$SR`  
    read -a machine_ip_list  <<< $machine_ip_str
    echo `ssh -l root ${machine_ip_list[0]} ls -l $current_dir` > BuildID_str
    BuildID=`cat BuildID_str|grep current|awk -F'-> ' '{print $2}'|awk '{print $1}'|sed 's/.overwrite//g'`
    echo "### buildID:",$BuildID
}

fix_overwrite_sh () {
    chmod +x ./overwrite.sh                           
    sudo sed -i "s/1350852_sls-backend-server_InitDependentSystem/$BuildID/g" ./overwrite.sh 
    sudo sed -i "s/sls-backend-server/$Service/g" ./overwrite.sh            
    sudo sed -i "s/InitDependentSystem#/$SR/g" ./overwrite.sh             
    sudo sed -i "s/init_dependent_system/$APP/g" ./overwrite.sh  
}

get_remote_varabiles () {
    restart_SR_cmd=`tail -n 1 overwrite.sh`
    remove_overwrite_cmd=`tail -n 5 overwrite.sh|head -n 1|awk -F'##### ' '{print $2}'`
    re_overwrite_dir=`tail -n 4 overwrite.sh|head -n 1|awk -F'##### ' '{print $2}'`
}

build_overwrite () {
    ## 用 `` 是为了让 保证  先让这个 shell 命令执行完，才执行下一条 shell 命令。
    scp_done=`scp ./overwrite.sh   root@$machine_ip:/$current_dir > /dev/null 2>&1 &`
    echo `ssh -l  root $machine_ip $overwrite_script` 
    ## for 遍历 
    for source_file in ${source_files_list[*]}
    do
        echo '## ip: '$machine_ip'  '$source_file >> source_file.txt
        scp_done=`scp  $source_file  root@$machine_ip:/$dest_dir > /dev/null 2>&1 &`
    done

    echo `ssh -l  root $machine_ip  rm -rf $current_dir'current/alread_installed'`  
    echo `ssh -l  root $machine_ip $restart_SR_cmd`  
}

remove_overwrite () {
    echo `ssh -l  root $machine_ip "$remove_overwrite_cmd > /dev/null 2>&1 &"`
    echo `ssh -l  root $machine_ip "$re_overwrite_dir > /dev/null 2>&1 &"`
}


main () {
    echo "## source" > source_file.txt
    echo "## machine_ip" > machine_ip.txt
    for machine_ip in ${machine_ip_list[*]}
    do
        echo $machine_ip >> machine_ip.txt
        if [ $scripts_option ]
        then
            remove_overwrite
            echo "### Remove overwrite, ip:$machine_ip  $remove_overwrite_cmd "
        elif [ $dest_dir ] && [ $source_files_list ]
        then 
            build_overwrite
            echo "### build ip="$machine_ip,' '$Service/$SR/$APP/$BuildID/'successfully!'
        fi
    done  
}

write_overwrite_sh
get_common_varabiles
fix_overwrite_sh
get_remote_varabiles
main
```