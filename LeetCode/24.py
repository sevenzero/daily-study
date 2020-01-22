#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time    : 2020/1/21 4:13 下午
@Author  : duanpy001
@File    : 24.py
@Link    : https://leetcode-cn.com/problems/swap-nodes-in-pairs/
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 迭代法
    def swapPairs(self, head: ListNode) -> ListNode:
        # 两个节点以下的链表直接返回
        if not head or not head.next:
            return head
        else:
            extra_head = ListNode(0)
            extra_head.next = head
            p, q = extra_head, head
            while q and q.next:
                t = q.next
                q.next = t.next
                p.next = t
                t.next = q
                p = q
                q = p.next
            return extra_head.next

    # 递归法
    def swapPairs_2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        first_node = head
        second_node = head.next
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node
        return second_node


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
    res = s.swapPairs_2(node1)
    while res:
        print(res.val)
        res = res.next
