def multiple_str(str1, str2):
    str1, str2 = str1[::-1], str2[::-1]
    res_list = []
    for m in range(len(str1)):
        for n in range(len(str2)):
            _sum = int(str1[m]) * int(str2[n])
            res_list = _sum_list(_sum, m+n, res_list)

    print res_list
    for i in range(len(res_list)):
        if i + 1 ==  len(res_list): res_list.append(0)
        res_list[i+1] = res_list[i] / 10 + res_list[i+1]
        res_list[i] = res_list[i] % 10 
    res = ''.join(str(i) for i in res_list)
    print res.rstrip('0')[::-1]
    


def _sum_list(_sum, _int, res_list):
    p0 = _sum % 10
    p1 = _sum / 10
    if len(res_list) < _int + 2: 
        res_list.append(0)
        res_list.append(0)
    res_list[_int] = p0 + res_list[_int]
    res_list[_int+1] = p1 + res_list[_int+1]
    return res_list

multiple_str('4611686018427387904','4611686018427387904')

## `21267647932558653966460912964485513216`

