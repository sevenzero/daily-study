#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time    : 2020/1/20 9:48 上午
@Author  : duanpy001
@File    : 20.py
@Link    : https://leetcode-cn.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {'}': '{', ']': '[', ')': '('}
        if len(s) == 0:
            return True
        stack = [s[0]]
        for c in s[1:]:
            if c in bracket_dict.keys():
                if len(stack) == 0 or stack[-1] != bracket_dict[c]:
                    return False
                stack = stack[:-1]
            else:
                stack.append(c)
        if len(stack) != 0:
            return False
        else:
            return True



if __name__ == '__main__':
    s = Solution()
    test_data = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    test_res = [True, True, False, False, True]
    for i in test_data:
        print(s.isValid(i))
