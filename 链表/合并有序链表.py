# -*- coding:utf-8 -*-
'''
while循环里，当一个链表已经都遍历完，而另一个链表还有多余节点的时候
应该使用elif来把多余的节点都挂上去，而不是else，这会使每一次循环都走到这里面去
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        p1 = pHead1
        p2 = pHead2
        if (not p1):
            return p2
        if (not p2):
            return p1
        
        if (p1.val <= p2.val):
            node = ListNode(p1.val)
            p1 = p1.next
        else:
            node = ListNode(p2.val)
            p2 = p2.next
            
        head = node

        while (p1 or p2):
            if (p1 and p2):
                if (p1.val <= p2.val):
                    node.next = p1
                    node = node.next
                    p1 = p1.next
                else:
                    node.next = p2
                    node = node.next
                    p2 = p2.next
            elif (p1):
                node.next = p1
                p1 = p1.next
            elif (p2):
                node.next = p2
                p2 = p2.next
                
        return head

head1 = ListNode(1)
phead1 = head1
head1.next = ListNode(3)
head1 = head1.next
head1.next = ListNode(5)

head2 = ListNode(2)
phead2 = head2
head2.next = ListNode(4)
head2 = head2.next
head2.next = ListNode(6)

list = Solution().Merge(phead1, phead2)

arr = []
while (list):
    arr.append(list.val)
    list = list.next

print arr