# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# solution found on leetcode
class Solution01(object):
    def isValidBST(self, root, lessThan = float('inf'), largerThan = float('-inf')):
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and \
               self.isValidBST(root.right, lessThan, max(root.val, largerThan))



class Solution00(object):

    def tree_recursion(self, tree, left= float('-inf'), right = float('inf')):

        if tree == None:
            return 1

        if left!= None:

            if tree.val <= left:
                return 0

        if right != None:
            if tree.val >= right:
                return 0

        if tree.left == None and tree.right == None:
            return 1



        left_new_l = left
        right_new_l = tree.val

        left_new_r = tree.val
        right_new_r = right




        if tree.left == None:

            if tree.val < tree.right.val:
                return self.tree_recursion(tree.right, left=left_new_r, right = right_new_r)
            else:
                return 0

        if tree.right == None:

            if tree.val > tree.left.val:
                return self.tree_recursion(tree.left, left=left_new_l, right = right_new_l)
            else:
                return 0


        if tree.left.val < tree.val and tree.right.val > tree.val:
            return self.tree_recursion(tree.left, left=left_new_l, right = right_new_l)*self.tree_recursion(tree.right, left=left_new_r, right = right_new_r)



    def isValidBST(self, root):

        """
        :type root: TreeNode
        :rtype: bool
        """

        if self.tree_recursion(root) == 1:

            return True
        
        else:
            return False






class Solution(object):
    def isValidBST(self, root, leftbound = float('-inf'), rightbound = float('inf')):

        if not root:
            return True

        if root.val <= leftbound or root.val >= rightbound:
            return False

        else:
            return self.isValidBST(root.left, leftbound=leftbound, rightbound=min(rightbound, root.val)) \
        * self.isValidBST(root.right, leftbound=max(leftbound, root.val), rightbound=rightbound)






l1 = TreeNode(15)
l2 = TreeNode(12)
l3 = TreeNode(-2147483648)
l1.left = l2
l1.right = l3

l4 = TreeNode(5)
l5 = TreeNode(1)
l6 = TreeNode(4)
l7 = TreeNode(3)
l8 = TreeNode(6)

l4.left = l5
l4.right = l6
l6.left = l7
l6.right = l8

l9 = TreeNode(0)
l10 = TreeNode(-1)
l9.left = l10


l11 = TreeNode(10)
l12 = TreeNode(5)
l13 = TreeNode(15)
l14 = TreeNode(6)
l15 = TreeNode(20)
l11.left = l12
l11.right = l13
l13.left = l14
l13.right = l15

sol = Solution()
print(sol.isValidBST(l11))






