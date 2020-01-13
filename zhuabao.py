import os
from scapy.all import sniff,wrpcap,Raw,IP,TCP
# https://www.jianshu.com/p/76fb8f7b916f

# from scapy.arch.windows import *
# https://blog.csdn.net/a649344475/article/details/81110957
# >>> sniff(filter="ip src www.baidu.com", prn=lambda x:x.summary(), count=3)
# >>> sniff(filter="", prn=lambda x:x.summary())
# >>> sniff(filter="", iface="WLAN",prn=lambda x:x.summary(),count=10)

def get_pcap(ifs,ip=None,size=100): 
    ''' 获取指定 ifs(网卡), 指定数量size 的数据包;
        如果有指定ip，则这里只接收tcp，80端口，指定ip的包 ''' 
    filter = "" 
    size = size
    if ip: 
        filter += "ip src %s and tcp and tcp port 80"%ip 
        dpkt = sniff(iface=ifs,filter=filter,count=size) 
    else: 
        dpkt = sniff(iface=ifs,count=size)
        # wrpcap("pc1.pcap",dpkt) # 保存数据包到文件 
    return dpkt


def get_ip_pcap(ifs,sender,size=100):
    ''' 获取指定 ifs(网卡), 指定发送方 sender(域名或ip) 的数据包
        size：(一次获取数据包的数量） '''
    if 'www.' in sender:
        v = os.popen('ping %s'%sender).read()
        ip = v.split()[8]
        print("准备接收IP为 %s 的数据包..."%ip)
    else:
        ip = sender
        print("准备接收IP为 %s 的数据包..."%ip)
    count = 0  
    while count<5:
        d = get_pcap(ifs,ip=sender,size=size)
        for i in d:
            print(" i  ", i)
            try:
                if i[IP].src==ip: # 发送方的IP为：ip  接收方的IP：i[IP].dst==ip
                    print(i[Raw].load)
            except:
                pass
        count+=1



def main():
    # get_pcap("WLAN",ip="192.168.1.109",size=100)
    ifs = 'WLAN' # 网卡   vEthernet (Default Switch)
    ip = "www.baidu.com"  # ip地址，也可写域名，如：www.baidu.com
    get_ip_pcap(ifs,ip,size=1)  # 一次接收一个包

if __name__ =='__main__':
    main()




















# #-*- coding:GBK -*-

# import os
def get_netiface():
    net_dict={}

    data=os.popen('ipconfig /all').readlines()

    for line in data:

        if "网适配器" in line:

            # print(line,"##############",line[line.index('器')+2:].split(':')[0],)

            interface=line[line.index('器')+2:].split(':')[0]

            net_dict[interface]=''

        if 'IPv4' in line:

            #print line.split(":")[1]

            ip=line.split(":")[1].strip().split('(')[0]

            net_dict[interface]=ip

    for net in net_dict.keys():

        print(net+":"+net_dict[net])

# get_netiface()