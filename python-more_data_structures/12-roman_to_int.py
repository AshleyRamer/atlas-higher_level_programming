#!/usr/bin/python3
def roman_to_int(roman_string):
    dic_r_i = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    if roman_string and isinstance(roman_string, str):
        int_num = 0
        int_list = []
        for r in roman_string:
            int_num += dic_r_i.get(r)
            int_list.append(dic_r_i.get(r))
            iterat = len(int_list) - 1
            if iterat > 0 and int_list[iterat - 1] < int_list[iterat]:
                int_num -= int_list[iterat - 1] * 2
        return int_num
    else:
        return 0
