#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time    : 2020/1/20 10:01 上午
@Author  : duanpy001
@File    : 21.py
@Link    : https://leetcode-cn.com/problems/merge-two-sorted-lists/
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
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

    def mergeTwoLists_2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists_2(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists_2(l1, l2.next)
            return l2





if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(3)
    # node2.next = node3
    node4 = ListNode(4)
    node3.next = node4
    node5 = ListNode(5)
    node4.next = node5
    s = Solution()
    res = s.mergeTwoLists(node1, node3)
    while res:
        print(res.val)
        res = res.next