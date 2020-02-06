# -*- coding:utf-8 -*-
'''
总体思路是没错的，大递归【找值相同的节点】里前序遍历，有一样的节点则把它们作为根节点，判断这两个根节点下的子节点是否一样
小递归【判断两个相同的节点是否连着相同的子树】也用前序遍历

易错点:
1. 遍历完b就算是一样了，a可能下面还连着其他节点，不能放入考虑
2. 大递归中会有当在第二层以及更深的递归中return true的时候会拿不到，所以每一次递归都要做判断
3. 大递归里传的节点，b应该一直是它的根节点本身!!
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        def core(pRoot1, pRoot2):
            def ifSubtree(a, b):
                if a and b:
                    if (a.val != b.val):
                        return False
                    if not ifSubtree(a.left, b.left):
                        return False
                    if not ifSubtree(a.right, b.right):
                        return False
                    return True
                elif b == None:
                    return True
                else:
                    return False
            if (pRoot1 and pRoot2):   
                if (pRoot1.val == pRoot2.val):
                    if (ifSubtree(pRoot1, pRoot2)):
                        return True
                if (core(pRoot1.left, pRoot2)):
                    return True
                if (core(pRoot1.right, pRoot2)):
                    return True
                
        if (core(pRoot1, pRoot2)):
            return True
        else:
            return False

root1 = TreeNode(8)
node1 = root1
root1.left = TreeNode(8)
root1.right = TreeNode(7)
node1 = node1.left
node1.left = TreeNode(9)
node1.right = TreeNode(2)
node1 = node1.right
node1.left = TreeNode(4)
node1.right = TreeNode(7)

root2 = TreeNode(8)
root2.left = TreeNode(9)
root2.right = TreeNode(2)

print(Solution().HasSubtree(root1, root2))