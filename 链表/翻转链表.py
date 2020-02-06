# -*- coding:utf-8 -*-
'''
l和r不要再搞错啦！！！
不然后期发现再修改会有很多遗漏的bug
'''


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if (not pHead):
            return None
        l = pHead
        if (not l.next):
            return l
        m = l.next
        if (not m.next):
            m.next = l
            return m
        r = m.next
        
        l.next = None
        
        while(m):
            m.next = l
            l = m
            m = r
            if (r):
                r = r.next
            
        return l