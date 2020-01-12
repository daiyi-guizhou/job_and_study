感谢(https://www.douban.com/note/264976536/)
1，获取Cookie
很简单，使用Chrome浏览器的”开发者工具(Developer Tools)“或者Firefox的"HTTPFOX"等插件就可以直接查看自己新浪微博的Cookie。（注： 这个私人Cookie千万不要泄露哦！）
比如，Chrome 查看cookie （快捷键F12 可以调出chrome开发者工具）![在这里插入图片描述](https://img-blog.csdnimg.cn/20181207164520470.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==,size_16,color_FFFFFF,t_70)2， 将Cookie作为访问微博的header参数提交
headers = {'cookie': 'your cookie'}
req = urllib2.Request(url, headers=headers) #每次访问页面都带上 headers参数
r = urllib2.urlopen(req)

```
import urllib2
import re

cookie = 'your-cookie'  # get your cookie from Chrome or Firefox
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0',
    'cookie': cookie
}

def visit():
    url = 'http://weibo.com'
    req = urllib2.Request(url, headers=headers)
    text = urllib2.urlopen(req).read()

    # print the title, check if you login to weibo sucessfully
    pat_title = re.compile('<title>(.+?)</title>')
    r = pat_title.search(text)
    if r:
        print r.group(1)

if __name__ == '__main__':
visit()
```
#以下是我用requests　访问的.
```
import requests
headers={'cookie':'mysession=XXXXXXX '}

req=requests.get('https://www.xxx.com/machineAlias',headers=headers)
print(req.text)
```
 下面是 urllib 用cookie
```
#####
# import urllib.request

# url = "http://www.renren.com"
# headers = {
#         "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#         #Accept-Encoding: gzip, deflate
#         "Accept-Language":"zh-CN,zh;q=0.9",
#         "Connection":"keep-alive",
#         "Cookie":"anonymid=jq7d42gh-gr2bw; depovince=BJ; _r01_=1; JSESSIONID=abcReukbdFRnJc41oCYFw; ick_login=2a4b43b1-f36e-4bc4-983b-d7f6b80bc3b7; first_login_flag=1; ln_uact=18633615542; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; loginfrom=syshome; ch_id=10016; jebe_key=f448d565-0c8d-4f43-b79c-002d5e47bae0%7C2e9beece3ead42fe6a26739d515f14df%7C1545960795286%7C1%7C1545960795988; wp_fold=0; jebecookies=fbce59e9-2a4b-42a2-9e63-5b0f10d2fc7b|||||; _de=2229A2704041535FC5E7FC3B0F076082; p=96d21992fd673d6af178f0583cf315e43; t=89f2de512578d793ac1593f83fa3dad83; societyguester=89f2de512578d793ac1593f83fa3dad83; id=969255813; xnsid=d88ce62",
#         "Host":"www.renren.com",
#         "Referer":"http://www.renren.com/SysHome.do",
#         "Upgrade-Insecure-Requests":"1",
#         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
#     }

# req = urllib.request.Request(url,headers=headers)
# res = urllib.request.urlopen(req)
# html = res.read().decode("utf-8")
# print(html)
```

#获取数据后分开，将一行转为多行．
```
 python3 cookie-al |awk -F"匹配正则" '{print $2}'|awk -F":" '{for (i=1;i<=NF;i++) printf "%s\n",$i}'| head -n 3
 ### awk '{ printf "%s "$0 }'　　#多行转一行
```

## 爬虫
#### 我遇到的坑
#第一次网址写错了，　
#方法用错了,get不行．需要用post
#需要用json格式的参数.
#第二次访问需要cookies,headers.后来发现不用cookies．　我也迷茫了．
（为了避免出错，还是带上吧．）
###以上这些都是前端设置好的．所以我们要获取数据，只能按照前端设置好的规则来，他需要什么参数，什么数据，我们就传什么数据给他．


```
#!/usr/bin/python3
import json
import requests
import sys

optCode=sys.argv[1]
print(sys.argv[1])
print(optCode)
payload = {'username':'xxx', 'password':'xxx'}

#第一次网址写错了，　
#方法用错了,get不行．需要用post
#需要用json格式的参数.


r = requests.post('https:///www.xxx.com/user/login', data=json.dumps(payload))　　
print("1  cookies:   ",r.cookies.get_dict())
print("2  cookies:   ",r.cookies)
print('^^^^^^^^^^^^^^^^^')
for cookie in r.cookies:　　　　＃　截取字典类型的值．
    cookieValue2='mysession='+cookie.value
print(cookieValue2)
print("r.status_code:   ",r.status_code)
print("r.request.body:  ",r.request.body)
print("r.headers:  ",r.headers)
print('text    ',r.text)
print("####################################################################################")
headersr2 = {'Content-Type': 'application/json;charset=utf-8',
           'Cookie': cookieValue2}

payload2 = {'username':'xxx', 'password':'xxx,'OtpCode':optCode}
#r2 = requests.get('https:///www.xxx.com/static/inspinia/css/style.css', data=payload2)　　＃网站错了，后来打开网站最初登录界面，一边打开开发者工具，一边登录，看到开发者工具中的变化，实时数据，才真正确定．
#r2 = requests.post('https:///www.xxx.com/user/login', data=payload2)   #需要json格式
#r2 = requests.post('https:///www.xxx.com/user/login', data=json.dumps(payload2),headers=headersr2)   #带headers访问.
#r2 = requests.post('https:///www.xxx.com/user/login',data=json.dumps(payload2),cookies=r.cookies)  #用cookies访问．
r2 = requests.post('https:///www.xxx.com/user/login',data=json.dumps(payload2))
print("r2.status_code:   ",r2.status_code)
print("r2.request.body:  ",r2.request.body)
print("1  cookies:   ",r2.cookies.get_dict())
print("2  cookies:   ",r2.cookies)
print('text    ',r2.text)
print("####################################################################################")
#r3 = requests.get('https:///www.xxx.com/Machine/list/v2',cookies=r2.cookies)
#head=r2.cookies.get_dict()
for cookie in r2.cookies:
    cookieValue3='mysession='+cookie.value
print(cookieValue3)
head = {'Content-Type': 'application/json;charset=utf-8',
           'Cookie': cookieValue3}
#r3 = requests.get('https:///www.xxx.com/machineAlias/v2',cookies=r2.cookies)
r3 = requests.get('https:///www.xxx.com/machineAlias/v2',headers=head)
print("r3.status_code:   ",r3.status_code)
print(r3.text)
```

## params请求
用开发者工具，看到的Request URL是，
https://falcon.xxx.com/api/endpoints?q=dm/&tags=cluster=detection-machine&limit=500&page=1&_r=0.43419260989925357
这时候，request的时候，就需要用params．
```
payload2 = {'q':"dm/",'tags':"cluster=detection-machine",'limit':'500','page':'1'}
r2 = requests.get('https://falcon.kkk.com/api/endpoints', params=payload2,cookies=r.cookies)
```
总体代码很简单

```
import json
import requests

payload = {'name':'test', 'password':'test','ldap':0}
r = requests.post('https://falcon.xxx.com/auth/login', data=payload)

payload2 = {'q':"dm/",'tags':"cluster=detection-machine",'limit':'500','page':'1'}
r2 = requests.get('https://falcon.xxx.com/api/endpoints', params=payload2,cookies=r.cookies)
print('text    ',r2.text)
```
## post的json数据

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190123182457189.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shaddow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTA4ODg5MQ==,size_16,color_FFFFFF,t_70)第一次看到这个参数，json 格式。 于是采用

```
data={
    'Args': 
    [
    {'0':"InstallDeb"},
    {'1':"netdiskFile/falcon_agent-20181220_0.2.5.deb"}    	
    ],
    'IsControlCmd':'true',
    'MachineIds':
    [
    {'0':"70-85-C2-81-D5-0E"}
    ]
}

req=requests.post('https://www.xxx.com/yyy/zzz',headers=headers,data=json.dumps(data))
```
结果 400报错， 格式不对。结果这个看不懂啊， 于是各种尝试。
最终

```
data={
    'Args': 
    [
    "InstallDeb",
   "netdiskFile/falcon_agent-20181220_0.2.5.deb"  	
    ],
    'IsControlCmd':True,
    'MachineIds':
    [
    "70-85-C2-81-D5-0E"
    ]
}
req=requests.post('https://www.xxx.com/yyy/zzz',headers=headers,data=json.dumps(data))
```
  Params里的参数， 0，1，2，全是干扰项。 不用管。  直接就是。{"Args":["InstallDeb",
   "netdiskFile/falcon_agent-20181220_0.2.5.deb" ]},"IsControlCmd":True,{"MachineIds":[ "70-85-C2-81-D5-0E"]}就可以了，直接列表[].    
 'IsControlCmd':True, 这个参数是True，是bool, 不是str.   
 
#### post中json的字符串。

```
data = {"query":{"match":{"imtype":"LTCUS"}},"sort":[{"rtdatetime":{"order":"desc"}}],"size":3}
 
headers = {'Content-Type':'application/json'}
request = urllib2.Request(url='http://159.138.1.196:9200/gspoc/idealmoney_rt_result/_search',headers=headers,data=json.dumps(data))
response = urllib2.urlopen(request)
 
print response.read()
```

```
#组装参数		
p["app_id"]="1106571733"
p["time_stamp"]=str(time.time())	
p["model"]="住嘉佳园"	
#发送post请求
r=requests.post("https://api.global.net/datastore/v1/tracks/",data=p)
#获取返回的json数据

print(r.json())
```

```
url = "https://XXXXX"
headers = {'UserName': 'XXXXX',
         'AccessToken': 'XXXXX' }

data={
        'UserName': 'XXXXX',
        'DeviceId': 'XXXXXXXXX',
        'AppVersion': 'XXXXX'
        'Datas': json.dumps
           (
           [
           {"DeviceId": "XXXXXXX",
            "DeviceType": "XXXXX",
            "Time": "2017-08-28 10:32:28",
            "TimeZone": 2
            "PhoneTime": "2017-08-28 10:32:28"},
             {json2},
             {json3}
         ]
         )
        }

r = requests.post(url, headers=headers, data=data)
```

****
****
***
# 用httplib模块
```
import requests
import socket
import httplib
import urllib
import json

def get_machine_sr_info():
    path = "/api/v5/GetMachineInfo"
    params = {
            "hostname": socket.gethostname(),
            "serverrole": "server.Nginx#",
            "action_name": "state",
        }
    client = httplib.HTTPConnection("127.0.0.1", "8089", True, 10)
    try:
        url = path
        if params:
            url += "?"
            url += urllib.urlencode(params)
        print("### url :",url)
        client.request("GET", url)
        resp = client.getresponse()
        print("####  :",str(resp.status))
        content = resp.read()
        res = json.loads(content)
        print("#### content :",content ," #### res.out :",res)
        #return res
    finally:
        client.close()
get_machine_sr_info()
```
```
$ sudo /home/tops/bin/python ./test.py
('### url :', '/api/v5/GetMachineInfo?hostname=rrrr&action_name=state&serverrole=server.Nginx%23')
('####  :', '200')
('#### content :', '{\n    "err_code": 61,\n    "err_msg": "not found"\n}', ' #### res.out :', {u'err_msg': u'not found', u'err_code': 61})
```
