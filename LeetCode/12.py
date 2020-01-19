#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time    : 2020/1/17 10:55
@Author  : duanpy001
@File    : 12.py
@Link    : https://leetcode-cn.com/problems/integer-to-roman/
           https://leetcode-cn.com/problems/roman-to-integer/
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        res = ''
        for i in range(len(numbers)-1, -1, -1):
            while num >= numbers[i]:
                num = num - numbers[i]
                res += roman[i]
        return res

    def romanToInt(self, s: str) -> int:
        roman_numbers = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        res = 0
        last_add = 0
        for c in s:
            if roman_numbers[c] > last_add:
                res -= 2 * last_add
            res += roman_numbers[c]
            last_add = roman_numbers[c]
        return res


if __name__ == '__main__':
    s = Solution()
    test_data = [3, 4, 58, 1994]
    test_res = ['III', 'IV', 'LVIII', 'MCMXCIV', ]
    for i in test_res:
        print(s.romanToInt(i))
