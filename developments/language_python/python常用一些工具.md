<!-- TOC -->

        - [yaml](#yaml)
        - [face_recognition](#face_recognition)
        - [获取token](#获取token)
- [yapf ,isort 格式化，排序你的代码](#yapf-isort-格式化排序你的代码)

<!-- /TOC -->

##### yaml   
(https://blog.csdn.net/qq_16912257/article/details/83025924)
打开和保存
```
import yaml
import json

result = yaml.load(open('demo.yml'))
print json.dumps(result, indent=2)
-----------------------------------------------------------
result = yaml.safe_dump(d, encoding='utf-8', allow_unicode=True, default_flow_style=False)
open('demo.yml', 'w').write(result)
——————————————————————
save_yaml('teacher_info_list ', teacher_info_list)
---------------------------------------------------------
with open(file_name+t+'.yaml', mode='w') as f:
        yaml.dump(data, f)
```
##### face_recognition
人脸识别工具 直接调用这个函数就好
##### 获取token
```
def get_token_emp(username, password):
    """get_token_emp
    获取token
    判断是否获取成功,
    status_code=200 有返回值.
    还需要做其他的操作.
    """
    token_api = '/connect/token'
    data = {
        'client_id': "video",
        'client_secret': "videosecrets",
        'grant_type': "password",
        'username': username,
        'password': password,
    }
    r = do_post(api=token_api, data=data)
    if 'access_token' in r:
        return r['access_token']
    else:
        return 0


def do_post(api, host=None, token=None, data=None):
    """post构建,header构建,通用返回值判断
    """
    host = emp_host
    url = 'http://' + host + api
    headers = {}
    if token:
        headers = {'Authorization': 'Bearer ' + token,  # 'Content-Type': 'application/json'
                   }
    result = re.post(url, data=data, headers=headers)
    if result.status_code != 200:
        print("something went wrong")
        return 0
    return result.json()
```
### yapf ,isort 格式化，排序你的代码
 python中有库，yapf (格式化),isort  （排序）两个结合，格式化你的代码。


