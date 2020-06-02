
class Solution(object):
    def findTheLongestSubstring(self, s):
        all_set_sort_dict = {}
        all_set_sort_dict['[]'] = -1
        current_list = []
        vowel_str="aeiou"
        max_len,current_len=0,0
        for i in xrange(len(s)):
            if s[i] in vowel_str:
                if s[i] not in current_list:
                    current_list.append(s[i])
                else:
                    current_list.remove(s[i])
                if str(current_list) in all_set_sort_dict.keys():
                    current_len = i - all_set_sort_dict[str(current_list)]
                else:
                    all_set_sort_dict[str(current_list)] = i
                    current_len = 0
            else:
                current_len = i - all_set_sort_dict[str(current_list)]
                print current_len
            if current_len > max_len:
                max_len = current_len
        return max_len
