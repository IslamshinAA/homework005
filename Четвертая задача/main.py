res_str = 'AAAAABdddddddBCCCfffffDD'


def calculate_s(s):
    new_str = ""
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
        new_str += str(count) + s[i]
        i = i + 1
    return new_str


print(calculate_s(res_str))
