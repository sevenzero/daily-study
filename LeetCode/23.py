#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time    : 2020/1/20 3:17 下午
@Author  : duanpy001
@File    : 23.py
@Link    : https://leetcode-cn.com/problems/merge-k-sorted-lists/
"""
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        l1 = lists[0]
        for l2 in lists[1:]:
            l1 = self.mergeTwoLists(l1, l2)
        return l1

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        t = head
        p, q = l1, l2
        while p and q:
            if p.val <= q.val:
                t.next = p
                p = p.next
            else:
                t.next = q
                q = q.next
            t = t.next
        if p:
            t.next = p
        else:
            t.next = q
        return head.next

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(3)
    node2.next = node3
    node4 = ListNode(4)
    # node3.next = node4
    node5 = ListNode(5)
    # node4.next = node5
    node6 = ListNode(6)
    node5.next = node6
    s = Solution()
    res = s.mergeKLists([node1, node4, node5])
    while res:
        print(res.val)
        res = res.next