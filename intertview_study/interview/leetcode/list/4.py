def findMedianSortedArrays(nums1, nums2):
    
    def get_element(k):
        in_k = k 
        last_1,last_2=0,0
        index_1,index_2=0,0
        move_k = k / 2

        while True:
            if move_k == 0:
                if k % 2 == 0:
                    return max(nums1[last_1-1],nums2[last_2-1])
                else:
                    return min(nums1[last_1-1],nums2[last_2-1])
            if last_1 > len(nums1):
                print "#2 ", nums2[(in_k - len(nums1) - 1)]
                return nums2[(in_k - len(nums1) - 1)]
            if last_2 > len(nums2):
                print "#3 ", nums1[(in_k - len(nums2) - 1)]
                return nums1[(in_k - len(nums2) - 1)]

            index_1 = min((index_1 + move_k -1 ),(len(nums1) -1))
            index_2 = min((index_2 + move_k -1 ),(len(nums1) -1))

            if nums1[index_1] < nums2[index_2]:
                last_1 = last_1 + move_k
                index_1 = index_1 + move_k 
                print "*",last_1  
            else:
                last_2 = last_2 + move_k
                index_2 = index_2 + move_k 
                print "**",last_2
            move_k = move_k / 2



    total_len = len(nums2) + len(nums1)

    if total_len % 2 == 0:
        print (get_element(total_len/2) + get_element(total_len/2 + 1))/2.0
    else:
        print get_element(total_len/2 + 1)


nums2 = [1,2,3]
nums1 = [3,4,5,6]
# nums2 = [1,2]
# nums1 = [3]
# nums2 = [1,2,3,4,5,6]
# nums1 = [0]
findMedianSortedArrays(nums1, nums2)