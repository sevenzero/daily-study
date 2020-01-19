#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time    : 2020/1/16 16:55
@Author  : duanpy001
@File    : 8.py
@Link    : https://leetcode-cn.com/problems/string-to-integer-atoi/
"""
class Solution:
    def myAtoi(self, str: str) -> int:
        symbol = ['+', '-']
        number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        int_max = 2147483648
        start_flag = False
        sign_flag = True
        res = ''
        for c in str:
            # 是数字或者在打头的正负号
            if c in number or (c in symbol and not start_flag):
                start_flag = True
                # 如果是正负号，相应的置sign_flag
                if c in symbol:
                    sign_flag = sign_flag & (c == '+')
                else:
                    res += c
            # 开头的空格过滤
            elif c == ' ' and not start_flag:
                continue
            else:
                break
        if res == '':
            return 0
        res = int(res) * (1 if sign_flag else -1)
        if res > int_max - 1:
            return int_max - 1
        elif res < -1 * int_max:
            return -1 * int_max
        else:
            return res


if __name__ == '__main__':
    s = Solution()
    test_data = ['-24',  '2 -12', ' ##2, -12', '-', '3.114', '   +-42', 'words and 987', '4193 with words 4', '-91283472332']
    for i in test_data:
        print(s.myAtoi(i))

