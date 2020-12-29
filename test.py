import sys
if __name__ == "__main__":
    raw_str = sys.stdin.readline().strip()
    
    _str_dict = {}.fromkeys((sys.stdin.readline().strip()))
    res = ""
    for word in raw_str:
        new_word = []
        for char in word:
            if char not in _str_dict.keys(): new_word.append(char)
        res = res + "".join(new_word)
    print(res.strip())