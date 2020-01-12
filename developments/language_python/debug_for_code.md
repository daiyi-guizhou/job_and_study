use  python or bash  line by line,one by one .


when you get a class.a deb,a file.  but with some bugs
you should debug. 


python 中 requests 模块  容易超时 ， 导致 发送失败，  设置超时时间后就好多了。 
```
  response = requests.request(
        "POST", url, data=json.dumps(payload), headers=headers, timeout=(10, 30))

```

