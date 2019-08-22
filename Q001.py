__author__ = 'linchin'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



# two sums
class Solution:
    def twoSum(self, l1, l2):

        dummy = sum = ListNode(0)

        carry = 0

        while l1 or l2 or carry:

            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            sum.next = ListNode(carry%10)
            sum = sum.next

            carry //= 10

        return dummy.next

























