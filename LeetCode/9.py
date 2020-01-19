#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time    : 2020/1/17 9:03
@Author  : duanpy001
@File    : 9.py
@Link    : https://leetcode-cn.com/problems/palindrome-number/
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]



if __name__ == '__main__':
    s = Solution()
    test_data = [1, 12, 121, -12, 10]
    for i in test_data:
        print(s.isPalindrome(i))
