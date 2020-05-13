#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time    : 2020/2/9 3:36 下午
@Author  : duanpy001
@File    : 25.py
@Link    : https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pass

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(3)
    node2.next = node3
    node4 = ListNode(4)
    node3.next = node4
    node5 = ListNode(5)
    node4.next = node5
    node6 = ListNode(6)
    node5.next = node6
    s = Solution()
    res = s.swapPairs_recursive(node1)
    while res:
        print(res.val)
        res = res.next
