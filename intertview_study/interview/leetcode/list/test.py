class Solution():
    def partition(self, _list, l, r):
        _init = _list[l]
        while l < r:
            while l < r and _init <= _list[r]:
                r = r -1
            _list[l]=_list[r]
            while l < r and _list[l] <= _init:
                l = l + 1
            _list[r]=_list[l]
        _list[l] = _init
        return l

    def getLeastNumbers(self, arr, k):
        def quick_sort(_list, low, high):
            # print _list
            if low < high:
                _val = self.partition(_list,low,high)
                quick_sort(_list,low, (_val-1))
                quick_sort(_list,(_val+1),high)

        quick_sort(arr,0,(len(arr) -1))
        return arr[:k]

















"""

def partition(_list, l, r):
    _init = _list[l]
    while l < r:
        while l < r and _init <= _list[r]:
            r = r -1
        _list[l]=_list[r]
        while l < r and _list[l] <= _init:
            l = l + 1
        _list[r]=_list[l]
    _list[l] = _init
    return l

def quick_sort(_list, low, high):
    # print _list
    if low < high:
        _val = partition(_list,low,high)
        quick_sort(_list,low, _val-1)
        quick_sort(_list,_val+1,high)
    # print '## ', low,high

arr=[0,0,1,2,4,2,2,3,1,4]
quick_sort(arr,0,len(arr) -1)
print arr[:8]



    

                
        ## over time
        # for i in xrange(k):
        #     flag = False
        #     print i 
        #     for j in xrange(len(arr)-1,i,-1):
        #         # print i,arr[j],arr[j-1],arr
        #         if arr[j] <= arr[j-1]:
        #             _val = arr[j-1]
        #             arr[j-1] = arr[j]
        #             arr[j] = _val
        #             flag = True
        #     if flag==False:
        #         break
        # return arr[:k]
"""