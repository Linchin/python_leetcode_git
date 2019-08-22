
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        me = ListNode(-1)

        temp = me

        while l1 and l2:


            if l1.val < l2.val:

                me.next = ListNode(l1.val)

                me = me.next

                l1 = l1.next

            else:

                me.next = ListNode(l2.val)

                me = me.next

                l2 = l2.next


        while l1:
            me.next = ListNode(l1.val)

            me = me.next

            l1 = l1.next


        while l2:


            me.next = ListNode(l2.val)

            me = me.next

            l2 = l2.next

        return temp.next


sol = Solution()

l1 = ListNode(0)
l1.next = ListNode(2)
l2 = ListNode(1)
l2.next = ListNode(2)


lm = sol.mergeTwoLists(l1, l2)

while lm:

    print(lm.val)
    lm = lm.next
