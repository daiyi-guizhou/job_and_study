class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        if len(matrix) == 1:
            return matrix[0]
        l,r,u,d,res = 0, len(matrix[0])-1,0,len(matrix)-1,[]
        while True:
            if l <= r:  ## l--r
                for i in range(l,r+1,1):
                    res.append(matrix[u][i])
                u = u + 1
            if u > d:
                break

            if u <= d: ## u --d
                for i in range(u, d+1,1):
                    res.append(matrix[i][r])
                r = r - 1
            if l > r:
                break

            if l <= r: ## r --l
                for i in range(r,l-1,-1):
                    res.append(matrix[d][i])
                d = d - 1
            if u > d :
                break

            if u <= d:
                for i in range(d,u-1,-1):
                    res.append(matrix[i][l])
                l = l + 1
            if l > r:
                break
        return res

"""
解题思路：
根据题目示例 matrix = [[1,2,3],[4,5,6],[7,8,9]] 的对应输出 [1,2,3,6,9,8,7,4,5] 可以发现，顺时针打印矩阵的顺序是 “从左向右、从上向下、从右向左、从下向上” 循环。

因此，考虑设定矩阵的“左、上、右、下”四个边界，模拟以上矩阵遍历顺序。


算法流程：
空值处理： 当 matrix 为空时，直接返回空列表 [] 即可。
初始化： 矩阵 左、右、上、下 四个边界 l , r , t , b ，用于打印的结果列表 res 。
循环打印： “从左向右、从上向下、从右向左、从下向上” 四个方向循环，每个方向打印中做以下三件事 （各方向的具体信息见下表） ；
根据边界打印，即将元素按顺序添加至列表 res 尾部；
边界向内收缩 11 （代表已被打印）；
判断是否打印完毕（边界是否相遇），若打印完毕则跳出。
返回值： 返回 res 即可。
打印方向	1. 根据边界打印	2. 边界向内收缩	3. 是否打印完毕
从左向右	左边界l ，右边界 r	上边界 t 加 11	是否 t > b
从上向下	上边界 t ，下边界b	右边界 r 减 11	是否 l > r
从右向左	右边界 r ，左边界l	下边界 b 减 11	是否 t > b
从下向上	下边界 b ，上边界t	左边界 l 加 11	是否 l > r
复杂度分析：
时间复杂度 O(MN)O(MN) ： M, NM,N 分别为矩阵行数和列数。
空间复杂度 O(1)O(1) ： 四个边界 l , r , t , b 使用常数大小的 额外 空间（ res 为必须使用的空间）。

作者：jyd
链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/solution/mian-shi-ti-29-shun-shi-zhen-da-yin-ju-zhen-she-di/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""