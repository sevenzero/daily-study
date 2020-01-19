#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time    : 2020/1/16 11:49
@Author  : duanpy001
@File    : 6.py
@Link    : https://leetcode-cn.com/problems/zigzag-conversion/
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [''] * min(numRows, len(s))
        cur_row = 0
        going_down = False
        for c in s:
            rows[cur_row] += c
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            cur_row += 1 if going_down else -1
        res = ''.join(rows)
        return res

    def convert_2(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        cycle_len = 2 * numRows - 2
        res = ''
        for i in range(numRows):
            for j in range(0, len(s) - i, cycle_len):
                # 相当于s[k * (2 * numRows-2) + i]，第一行最后一个字符索引最大值为len(s)-1-numRows
                res += s[i + j]
                # 对于中间行，
                if i != 0 and i != numRows - 1 and j + cycle_len - i < len(s):
                    # 此时的j = k * cycle_len = k * (2 * numRows-2)
                    # s[j + cycle_len - i] 相当于s[(k + 1) * (2 * numRows-2) - i]
                    res += s[j + cycle_len - i]
        return res

    def convert_3(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        cycle_len = 2 * numRows - 2
        res = ''
        for i in range(numRows):
            for j in range(0, len(s) - i, cycle_len):
                # 相当于s[k * (2 * numRows-2) + i]，第一行最后一个字符索引最大值为len(s)-1-numRows
                res += s[i + j]
                # 对于中间行，
                if i != 0 and i != numRows - 1 and j + cycle_len - i < len(s):
                    # 此时的j = k * cycle_len = k * (2 * numRows-2)
                    # s[j + cycle_len - i] 相当于s[(k + 1) * (2 * numRows-2) - i]
                    res += s[j + cycle_len - i]
        return res


if __name__ == '__main__':
    s = Solution()
    test_data = [('LEETCODEISHIRING', 3), ('LEETCODEISHIRING', 4), ("PAYPALISHIRING", 4)]
    test_res = ['LCIRETOESIIGEDHN', 'LDREOEIIECIHNTSG', 'PINALSIGYAHRPI']
    for i in test_data:
        print(s.convert_2(i[0], i[1]))
