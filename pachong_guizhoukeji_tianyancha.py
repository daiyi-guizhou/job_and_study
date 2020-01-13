#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests 
import urllib
import time 
import json
import random
import subprocess

def geturltoutf8(srcString):
    unquotedString = urllib.unquote(srcString)
    #print repr(unquotedString)
    textString = unquotedString.decode('utf-8')
    #print textString
    return textString 

# guiZhou = geturltoutf8("贵州科技")
guiZhou = "贵州科技"
sEncodeMsg = guiZhou.encode('utf-8')
headers={'cookie':'mysession=TYCID=4cf9d9a065c711e89c4ab79d1291dc16; undefined=4cf9d9a065c711e89c4ab79d1291dc16; ssuid=6624427005; jsid=SEM-BAIDU-PP-VIshenzhen-000873; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1561984711,1562027816; _ga=GA1.2.796895975.1561984712; _gid=GA1.2.1586310804.1561984712; bannerFlag=undefined; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1562027816; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E6%2589%2598%25E5%25AF%2586%25E5%258B%2592%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%252253%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODg2MjI0Nzg1NCIsImlhdCI6MTU2MjAyNzg2MywiZXhwIjoxNTkzNTYzODYzfQ.TxucX1k2xFAfXMbhbR4XwlT20kmGOlRWw_jDznpIFuKS2EvDe0nTXgwKCg5xkC9dzZV4sbmXG6ToKiRiAmQcuw%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218862247854%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODg2MjI0Nzg1NCIsImlhdCI6MTU2MjAyNzg2MywiZXhwIjoxNTkzNTYzODYzfQ.TxucX1k2xFAfXMbhbR4XwlT20kmGOlRWw_jDznpIFuKS2EvDe0nTXgwKCg5xkC9dzZV4sbmXG6ToKiRiAmQcuw; aliyungf_tc=AQAAAN2/JUHVZgUAb410cbDxTDg7SoMa'} 
# headers={'cookie':'mysession=TYCID=4cf9d9a065c711e89c4ab79d1291dc16; undefined=4cf9d9a065c711e89c4ab79d1291dc16; ssuid=6624427005; aliyungf_tc=AQAAAMaQ8mHB+QQAlbYPt5IQqaxy8/k1; csrfToken=vZTh1pyKI015bdhgCwLDN6gE; jsid=SEM-BAIDU-PP-VIshenzhen-000873; bannerFlag=undefined; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1561984711; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1561984759; _ga=GA1.2.796895975.1561984712; _gid=GA1.2.1586310804.1561984712; token=5782575860a24a5fb51fe918f2bdb3df; _utm=1f6b2e210ee540559343319195e25124; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E6%2589%2598%25E5%25AF%2586%25E5%258B%2592%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A0%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%252253%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODg2MjI0Nzg1NCIsImlhdCI6MTU2MTk4NDc1MCwiZXhwIjoxNTkzNTIwNzUwfQ.owpWZJaYH-dXoigKd-KAuSf2Op1ns5xarRtPyoB02pB5nhhkC_-DiInFSMWHeB7DePe_tFl490Vfcx9NiJsStQ%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218862247854%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODg2MjI0Nzg1NCIsImlhdCI6MTU2MTk4NDc1MCwiZXhwIjoxNTkzNTIwNzUwfQ.owpWZJaYH-dXoigKd-KAuSf2Op1ns5xarRtPyoB02pB5nhhkC_-DiInFSMWHeB7DePe_tFl490Vfcx9NiJsStQ'} 
# headers={'cookie':'mysession=aliyungf_tc=AQAAABqomXD6gQ4AwQEN3ayZFay1Ythz; ssuid=5083515037; bannerFlag=undefined; csrfToken=kLXc2RY4psjXXbdf_moqrET0; TYCID=6a1bd9b08f7011e9bb0ae1f5d8c7846a; undefined=6a1bd9b08f7011e9bb0ae1f5d8c7846a; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1560604857; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1560604964; _ga=GA1.2.733340950.1560604857; _gid=GA1.2.1066415593.1560604857; RTYCID=99c213b00d934cfcad6533f10fcf616a; CT_TYCID=4b21c036c56d4536a8e2c8d9ecab1fe3; cloud_token=4176018aad674c48a5f52fead2177574; cloud_utm=35924b8b851248f3af36f292e3308fc5; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E7%2590%25BC%25C2%25B7%25E6%259D%25B0%25E7%2589%25B9%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%252247%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTU4NTEyOTU5MiIsImlhdCI6MTU2MDYwNDk1MiwiZXhwIjoxNTkyMTQwOTUyfQ.SUzI3jVP7P9EW-Qb_kpE8GQSb_ZIV46VdfmOMSHqCgOoRDtJN8oRkc9fiZ5LvuvKtav3xfNRwfboEUtnNX0eaw%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252215585129592%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTU4NTEyOTU5MiIsImlhdCI6MTU2MDYwNDk1MiwiZXhwIjoxNTkyMTQwOTUyfQ.SUzI3jVP7P9EW-Qb_kpE8GQSb_ZIV46VdfmOMSHqCgOoRDtJN8oRkc9fiZ5LvuvKtav3xfNRwfboEUtnNX0eaw'} 
# headers={'cookie':'mysession=aliyungf_tc=AQAAABqomXD6gQ4AwQEN3ayZFay1Ythz; ssuid=5083515037; bannerFlag=true; csrfToken=kLXc2RY4psjXXbdf_moqrET0; TYCID=6a1bd9b08f7011e9bb0ae1f5d8c7846a; undefined=6a1bd9b08f7011e9bb0ae1f5d8c7846a; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1560604857,1560612797; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1560613527; _ga=GA1.2.733340950.1560604857; _gid=GA1.2.1066415593.1560604857; RTYCID=99c213b00d934cfcad6533f10fcf616a; CT_TYCID=4b21c036c56d4536a8e2c8d9ecab1fe3; cloud_token=4176018aad674c48a5f52fead2177574; token=ef9f6b2a6a62424b801800ca33fccff9; _utm=0c0560531bf743f7abcc969e22005677; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E5%25A4%259A%25E6%2581%25A9%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25221%2522%252C%2522monitorUnreadCount%2522%253A%2522144%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODY4NTAwMDY1NCIsImlhdCI6MTU2MDYxMzUyOCwiZXhwIjoxNTkyMTQ5NTI4fQ.6FmjYlUDgJzRUew1bMHEHRm3ccyWjfil84OKKLJOdXKy_T3f299dSRbCfuyO6AWgiou9BGPX3xhQbZVjXInr1Q%2522%252C%2522pleaseAnswerCount%2522%253A%25221%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218685000654%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODY4NTAwMDY1NCIsImlhdCI6MTU2MDYxMzUyOCwiZXhwIjoxNTkyMTQ5NTI4fQ.6FmjYlUDgJzRUew1bMHEHRm3ccyWjfil84OKKLJOdXKy_T3f299dSRbCfuyO6AWgiou9BGPX3xhQbZVjXInr1Q; _gat_gtag_UA_123487620_1=1'}
req=requests.get('https://www.tianyancha.com/search?key=贵州科技&rnd=',headers=headers) 
# print(req.text)
t1 = int(time.time() * 1000)
_t1 = t1 - random.randint(100,1000)
imgUrl = "https://antirobot.tianyancha.com/captcha/getCaptcha.json?"
imgUrl = imgUrl + "t=" + str(t1) + "&_=" + str(_t1)
reqImage=requests.get(imgUrl,headers=headers)
kk = eval(reqImage.text)
print(type(kk)) 
# print(kk["data"]["bgImage"])
imageUrl = "data:image/jpeg;base64," + kk["data"]["bgImage"]  #base64编码的jpeg图片数据
# print(imageUrl)
subprocess.getoutput("wget {}".format(imageUrl))
codeimage = requests.get(imageUrl)
with open("C:\\Users\\戴义\Downloads","wb") as f:
    f.write(codeimage.content)
    print("ok   codeimage is ok")




# with open('page1', 'w+') as f:
#         f.write(req.text)

# for i in range(2,3): #251
#     # time.sleep(30)
#     urlPage = 'https://www.tianyancha.com/search/p' + str(i)+ '?key=贵州科技&rnd='
#     filename = "22page" + str(i)
#     print(urlPage)
#     req=requests.get(urlPage,headers=headers) 
#     if i % 100 == 0:
#         print(req.text)
#     # filetest = str(req.text.encode('GB18030'))
#     with open(filename, 'w+') as f:
#         json.dump(req.text, f)
    #     f.write(req.text)

    # 
    # with open(filename, 'r+') as f:
    #     json.dump(req.text, f)



# :https://www.tianyancha.com/search/p2?key=贵州科技&rnd=
# https://www.tianyancha.com/search?key=贵州科技&rnd=

# https://antirobot.tianyancha.com/captcha/verify?return_url=https://www.tianyancha.com/vipintro/?jsid=SEM-BAIDU-PP-VIshenzhen-000873&rnd=
# https://antirobot.tianyancha.com/captcha/getCaptcha.json?t=1562034361673&_=1562034361389
# t=1562034361673&_=1562034361389
#   1562034361389
#   284
# t=1562035136475&_=1562035136335
#   1562035136335
#   140

# {"state":"ok","message":"","special":"","data":{"id":"6e49c7d7-3c25-452c-b6e0-df26dc1e9010","bgImage":"/9j/4AAQSkZJRgABAgAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0a\nHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIy\nMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABkAUADASIA\nAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQA\nAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3\nODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWm\np6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEA\nAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSEx\nBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElK\nU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3\nuLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwCssq1M\nsq1CYW7ULG/pXzXMfW2LayVID71VVH9M/hUgV/7pH4UuYLFgS7akjuF71XCbv/1U4W7f5FK47FwH\nd6Gl2L6VWWKVfX8KmXf70XFYnG2msnfr/OkUP6VPb21xdSiOKNmPfapbaPU4BOKaTb0E2krsZb2/\n2mdIYhmVzhQWC5P1NT3djLp1y0E67XHQjow9R7UXV4LWzk0nUbb7Zpt4C1jdaYwdpJcYKZ6Ek5HT\nj37WtP1Qi0ji1pZryIYtbi7ZRtsHJIVWYjlgCNz44IXJORXUsPdeZwvGJS8imqrTsLVi/wBLutOI\nY4kt3P7uZDlXHUfT/PWqgf1Nc8ouLsztjJSV0J5fz/yp/wBymmXb0pRNuqbDuIztTAzVN8rUg2rT\n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\nrj60UVAj/9k=","targetImage":"/9j/4AAQSkZJRgABAgAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0a\nHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIy\nMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAeAUADASIA\nAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQA\nAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3\nODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWm\np6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEA\nAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSEx\nBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElK\nU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3\nuLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD1qiii\nuY9EKKKKACiiigAooooAKhurq3srd7i7niggTG6SVwqrk4GSeOpAqavP/E6jVNdFnq0bR2JZI4rG\nHU0juLwhshjG0gTymOQMfvMqOnQa0aanKzehE5cq0PQKK88n8Ua1oYlS6uoptkct9u1CEQl4fM2w\nwKy7cSuiSvgpnPG3g47XRr6TVNFs9QlgWBrmFZhGsm8KGGRzgc4Izx19etOpQlBcz2CNRSdi9RRR\nWJYUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFcJ4v1xl8RabpdtqFxpN1bzJcT3UkgWBrN\nldXY53JncFQeYo+dlx1zTSuwO7orhB4xv9PTWbjyE1DRtHmW2mvZ7lIbiSQH97tQIqMV3KoX5d2O\nCxbjtbO4+12UFz5M0PnRrJ5Uy7XTIztYdiOhHrQ4tATUUUUgCiiigAooooAKKKKACiiigAooooAK\nKKKACiiigBksiwwvKwYqiliEQs2B6AZJPsOa4LULGTV77xA1ppt5fyalbQ20Ul7a/Z4rMcg4aXDk\nBh5hCIeQO5yPQKK1pVfZ6rciUebc888Oabbf25aabb6jLNYWVg6XVpKXhaWU7R+8tXwPLKyZBC8t\nkszE5PoEUUcEKQwxrHFGoVEQYVQOAAB0FVJ9H0+51a11WW2Vr61VlhmBIZQwIIOOo5PXOMnHWr1O\ntV9o0whDlCiiisSwooooAKKKKACiiigAooooAKKKKACiiigAooooAhvI55rKeK2uPs9w8bLFNsD+\nWxHDbTwcHnB61y0+iaxp86akJE1u6khSzuzsW2uGgySTC6soRg7s2OMqqDIZdzdfRTTsB5RcxSm4\nsdKV7ua0bUZJhoGq28kTzZk+bNwA6zokjebgbsoSWLbRXq9Yem+FrTT9Q+2vdX19LG0jWxvp/ONq\nHwGEbEbsEKo5JOAcH5mzuU5O4BRRRUgFFFFABRRRQAUUUUAf/9k=","userIp":"113.116.141.99","currentTime":"2019-07-02 10:26:03","mobile":"18862247854"}

# 1、天眼查和启信宝哪一个的数据更难爬呢？

# 其实在准备爬天眼查数据的时候，我对启信宝、企查查类似的网站分布从数据的完整性和数据的更新及时性分析了，结果个人觉得天眼查的数据比其他网站的要完整，数据维度要多一些，数据更新的时候也比较快，所以最后选择了爬取天眼查里面的企业数据。

# 2、天眼查的30个核心数据维度：

# 首先整个网站有主要核心数据有以下19大模块：1基本信息、2法人代表、3主要成员、4股东&出资、5变更记录、6公司年报、7司法风险、8舆情事件、9岗位招聘、10商品信息、11网站备案、12商标数据、13专利数据,、14 作品著作权软件著作权、16对外投资关系、17税务评级、18行政处罚、19进出口信用、20企业评级信用等十九个维度的企业数据，如果把这些数据爬下来，并且结构化，实现可以查询可以检索使用，可以导出到excel，可以生成企业报告，那么需要建立数据库来存储这些数据，像这种非结构化的数据我们选择mongdb数据库是最合适的。

#     采集速度太频繁了，会被封IP问题 怎么解决

# 当我们发出去的http请求到天眼查网站的时候，正常情况下返回200状态，说明请求合法被接受，而且会看到返回的数据，但是天眼查有自己的一套反爬机制算法，如果检查到同一个IP来不断的采集他网站的数据，那么他会被这个IP列入异常黑名单，您再去采集它网站数据的时候，那么就永远被拦截了。怎么解决这个问题呢，其实很简单，没有错用代理IP去访问，每一次请求的时候都采用代理IP方式去请求，而且这个代理IP是随机变动的，每次请求都不同，所以用这个代理IP技术解决了被封的问题。

# 4 天眼查2个亿的数据量怎么存储？需要多少的代理IP

# 我在写爬虫去爬天眼查的时候，刚开始使用网上的免费或者收费的代理IP，结果90%都被封号，所以建议大家以后采集这种大数据量网站的时候 不要使用网上免费的或者那种收费的IP，因为这种ip几秒钟就会过期，意思就是你没有采集网或者刚刚访问到数据的时候，这个IP就过期了导致你无法采集成功，所以最后我自己搭建了自己的代理池解决了2个亿天眼查数据的采集封IP问题。

# 5 天眼查网站数据几个亿数据的存储

# 数据库设计很重要，几个亿的数据存储 数据库设计很重要

# 我当时花了10天时间吧天眼查爬虫系统全部开发完毕，可以每天爬去百万条数据，30个维度的数据，数据爬下来后主要是数据的存储和管理，数据库的我采用了mongdb，爬虫开发技术我采用了python，几个亿的数据后台管理系统我采用php，我自己架构了分布式架构系统，所以我采集的我采用分布式+多线程+集群的方式，采集速度相当的快！

# python3 模拟请求目标网站：

# 我自己封装了一个方法，把请求头参数拼接后，然后调用requests的get方法直接模拟请求到目标网站，然后根据页面返回的关键词来识别是请求失败或者成功或者是被封了

# def get_html(url, mheaders={}, cookies={}):

# while True:

# try:

# proxy = get_proxy() # 获取代理

# if not mheaders:

# resp = requests.get(url, headers=headers, cookies=cookies, proxies=proxy, timeout=3)

# else:

# resp = requests.get(url, headers=mheaders, cookies=cookies, proxies=proxy, timeout=3)

# if 'tianyancha' in url:

# if resp.status_code == requests.codes.ok:

# if '请输入验证码' not in resp.text:

# return resp.text

# else:

# print('{}被封了！'.format(proxy))

# elif '融资历史' in resp.text:

# return resp.text

# else:

# print('错误的代码编号：{}, url:{}'.format(resp.status_code, url))

# else:

# if resp.status_code == requests.codes.ok:

# if '小查为' in resp.text or '基本信息' in resp.text:

# return resp.text

# else:

# print('错误的代码编号：{}, url:{}'.format(resp.status_code, url))

# except Exception as e:
# print('url :{},错误：{}'.format(url, e)))