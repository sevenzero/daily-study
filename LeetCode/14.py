#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time    : 2020/1/17 11:25
@Author  : duanpy001
@File    : 14.py
@Link    : https://leetcode-cn.com/problems/longest-common-prefix/
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                s += i[0]
            else:
                break
        return s

    def longestCommonPrefix_1(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        long_common_prefix = strs[0]
        for s in strs[1:]:
            while s.find(long_common_prefix) != 0:
                long_common_prefix = long_common_prefix[:-1]
                if long_common_prefix == '':
                    return ''
        return long_common_prefix

    def longestCommonPrefix_2(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        s = strs[0]
        for t in strs[1:]:
            long_common_prefix = ''
            for p, q in zip(s, t):
                if p == q:
                    long_common_prefix += p
                else:
                    break
            s = long_common_prefix
        return s

    def longestCommonPrefix_3(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]

    def longestCommonPrefix_4(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        return self.split_list(strs, 0, len(strs)-1)

    def split_list(self, strs, start, end):
        if start == end:
            return strs[start]
        else:
            middle = (end + start) // 2
            left_str = self.split_list(strs, start, middle)
            right_str = self.split_list(strs, middle + 1, end)
            return self.get_common_prefix(left_str, right_str)

    def get_common_prefix(self, s, t):
        min_len = min(len(s), len(t))
        for i in range(min_len):
            if s[i] != t[i]:
                return s[:i]
        return s[:min_len]


if __name__ == '__main__':
    s = Solution()
    test_data = [["flower", "flow", "flight"], ["dog", "racecar", "car"], ['aa', 'a']]
    test_res = ["fl", ""]
    for i in test_data:
        print(s.longestCommonPrefix_4(i))
