# 3  用 python实现快排：
# 快排的主函数，传入参数为一个列表，左右两端的下标


def QuickSort(list, low, high):
    if high > low:
        # 传入参数，通过Partitions函数，获取k下标值
        k = Partitions(list, low, high)
        # 递归排序列表k下标左侧的列表
        QuickSort(list, low, k-1)
        # print("*************  1  **** ")
        # 递归排序列表k下标右侧的列表
        QuickSort(list, k+1, high)
        # print("*************  ")


def Partitions(list, low, high):
    print(list)
    left = low
    right = high
    # 将最左侧的值赋值给参考值k
    k = list[low]
    # 当left下标，小于right下标的情况下，此时判断二者移动是否相交，若未相交，则一直循环
    while left < right:
        # 当left对应的值小于k参考值，就一直向右移动
        while list[left] <= k:
            left += 1
        # 当right对应的值大于k参考值，就一直向左移动
        while list[right] > k:
            right = right - 1
        # 若移动完，二者仍未相遇则交换下标对应的值
        if left < right:
            list[left], list[right] = list[right], list[left]
    # 若移动完，已经相遇，则交换right对应的值和参考值
    list[low] = list[right]
    list[right] = k
    # 返回k值
    print("############ K =   ",k)
    return right


list_demo = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
print(list_demo)
QuickSort(list_demo, 0, 9)
print(list_demo)


# Redis hash的个数???
# 总共有2的14次方，16384个哈希槽   https://www.cnblogs.com/zhuifeng-mayi/p/9306998.html
# Redis hash 是一个string类型的field和value的映射表，hash特别适合用于存储对象。
# Redis 中每个 hash 可以存储 2^32 - 1 键值对（40多亿）

# redis数据库的数量是可以配置的(修改配置文件)，默认情况下是16个

# 由于Redis的数据都存放在内存中，如果没有配置持久化，redis重启后数据就全丢失了，
# 于是需要开启redis的持久化功能，将数据保存到磁盘上，当redis重启后，可以从磁盘中恢复数据。
# redis提供两种方式进行持久化，一种是RDB持久化（原理是将Reids在内存中的数据库记录定时dump到磁盘上的RDB持久化），
# 另外一种是AOF（append only file）持久化（原理是将Reids的操作日志以追加的方式写入文件）


# Redis数据库支持的数据类型   str, hash ,list ,set ,sorted set.
#  Redis的过期策略:   定期删除+惰性删除
#  内存淘汰机制

# 如何避免hash槽中key出现相同的情况
# ,相同的key，其hashCode一定一样，那么put时回去同一桶链表中寻找，而在源码中put的时候如果key和hashCode都与之前存在的节点一样，那么会用新的value覆盖旧的value,并且put方法返回旧value的值
# ，但是有可能会有相同的Hash值，这个时候同一个位置上就是用链表的方式来存储。

# 一、工作场景
# （1）MySQL数据库每晚12:00自动完全备份。
# （2）某天早上上班，9点的时候，一同事犯晕drop了一个数据库！
# （3）需要紧急恢复！可利用备份的数据文件以及增量的binlog文件进行数据恢复。

# 二、数据恢复思路
# （1）利用全备的sql文件中记录的CHANGE MASTER语句，binlog文件及其位置点信息，找出binlog文件中增量的那部分。
# （2）用mysqlbinlog命令将上述的binlog文件导出为sql文件，并剔除其中的drop语句。
# （3）通过全备文件和增量binlog文件的导出sql文件，就可以恢复到完整的数据。


# hash  简单的说就是一种将任意长度的消息压缩到某一固定长度的消息摘要的函数。


# mongodb   文件型， 网站数据，

# nginx 比 apache快的原因
# 1：在高并发的情况下nginx比apache快，低并发体现不明显
# 2：快的原因得益于nginx的epoll模型  （apache 是阻塞模式， nginx是 异步非阻塞）
# https://baijiahao.baidu.com/s?id=1612594086537323804&wfr=spider&for=pc

# 简单的说，RPC就是从一台机器（客户端）上通过参数传递的方式调用另一台机器（服务器）上的一个函数或方法（可以统称为服务）并得到返回的结果。
    # RPC 会隐藏底层的通讯细节（不需要直接处理Socket通讯或Http通讯）
    # RPC 是一个请求响应模型。客户端发起请求，服务器返回响应（类似于Http的工作方式）
    # RPC 在使用形式上像调用本地函数（或方法）一样去调用远程的函数（或方法）

# 　　即能够调用远程规定好的接口就可称之为RPC！在我上一篇文章中所讲的Web service（SOAP）也是RPC的一种实现方式。