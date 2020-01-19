#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time    : 2020/1/17 9:12
@Author  : duanpy001
@File    : 10.py
@Link    : https://leetcode-cn.com/problems/regular-expression-matching/
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0 and len(p) == 0:
            return True
        if len(s) > 0 and len(p) == 0:
            return False
        if len(p) > 1 and p[1] == '*':
            if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
            else:
                return self.isMatch(s, p[2:])
        if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
            return self.isMatch(s[1:], p[1:])
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    test_data = [('aa', 'a'), ("aa", 'a*'), ("ab", '.*'), ("aab", "c*a*b"), ("mississippi", "mis*is*p*.")]
    for i in test_data:
        print(s.isMatch(i[0], i[1]))
