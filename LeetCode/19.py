#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time    : 2020/1/19 4:31 下午
@Author  : duanpy001
@File    : 19.py
@Link    : https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        p = head
        len_listNode = 0
        # 求链表长度
        while p:
            len_listNode += 1
            p = p.next
        # 如果是删除第一个节点，直接返回第二个节点
        if len_listNode == n:
            return head.next
        # 一直走到需要移除节点的上一个
        p = head
        for i in range(len_listNode - n - 1):
            p = p.next
        # 因为说过了 n 一定是合法的，所以p 一定不会指向最后一个节点
        p.next = p.next.next
        return head

    def removeNthFromEnd_2(self, head: ListNode, n: int) -> ListNode:
        p = q = head
        # 快指针先走 n 步
        for i in range(n):
            q = q.next
        # 如果快指针指向空了，说明需要删除头结点，直接返回
        if not q:
            return head.next
        # 快慢指针同步后移，当快指针走到最后一个节点时，慢指针刚好指向要删除节点的前一个节点
        while q.next:
            p = p.next
            q = q.next
        p.next = p.next.next
        return head


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
    s = Solution()
    res = s.removeNthFromEnd_2(node1, 5)
    while res:
        print(res.val)
        res = res.next
