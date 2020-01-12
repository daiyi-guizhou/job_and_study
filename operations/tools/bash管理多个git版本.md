
```
#!/bin/bash

function git_method()
{   
    for i in ${dir_list[*]};
    do 
        cd  $i
        echo `pwd`
        echo "         "
        branch=`git branch --show-current`;
        if [[ $local_branch==$branch ]];
        then 
            git checkout $origin_branch && git pull origin $origin_branch && echo "pull from $origin_branch";
        elif [[ $branch==$origin_branch ]]; 
        then 
            git pull origin $origin_branch && echo "pull from $origin_branch"; 
        else 
            echo "no current branch"; 
        fi;
        git checkout $local_branch;git merge -m "ok ,merge from $origin_branch" --stat $origin_branch;
        echo "              "
        echo "              "
        echo "              "
    done
}
# #########################################################
# #########################################################
# agility-live agility-live-daiyi-dev

dir_list[0]=/Users/daiyi/work-alibaba/git-work/enterPrise-EDITION/sls_j/product-sls 
dir_list[1]=/Users/daiyi/work-alibaba/git-work/enterPrise-EDITION/sls_j/service-sls-backend-server
origin_branch="agility-live"
local_branch="agility-live-daiyi-dev"
git_method

# #########################################################
# #########################################################
# master master-daiyi-dev
unset dir_list
dir_list[0]=/Users/daiyi/work-alibaba/git-work/sls-service-test
dir_list[1]=/Users/daiyi/work-alibaba/git-work/sls-tianji-app
dir_list[2]=/Users/daiyi/work-alibaba/git-work/enterPrise-EDITION/sls_j/product-sls 
dir_list[3]=/Users/daiyi/work-alibaba/git-work/enterPrise-EDITION/sls_j/service-sls-backend-server
origin_branch="master"
local_branch="master-daiyi-dev"
git_method

# #########################################################
# #########################################################
# ## live live-daiyi-dev
unset dir_list
dir_list[0]=/Users/daiyi/work-alibaba/git-work/enterPrise-EDITION/sls_j/service-sls-backend-server
origin_branch="live"
local_branch="live-daiyi-dev"
git_method

# #########################################################
# #########################################################
# ## v3.11xR v3.11xR-daiyi
unset dir_list
dir_list[0]=/Users/daiyi/work-alibaba/git-work/sls-tianji-app
origin_branch="v3.11xR"
local_branch="v3.11xR-daiyi-dev"
git_method
```
