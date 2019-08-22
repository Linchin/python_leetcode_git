# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None:
            return head

        if head.next == None:
            return head


        dummy = head.next

        iterator = head

        forehead = ListNode(0)

        while iterator:

            # alter links

            if iterator.next == None:
                break

            temp = iterator.next.next
#            if temp:
#                print(temp.val)

            forehead.next = iterator.next


            iterator.next.next = iterator

            forehead = iterator

            iterator.next = temp

            iterator = temp
#            if iterator:
#                print(iterator.val)


        return dummy



sol = Solution()


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l1.next = l2
l2.next = l3
#l3.next = l4

ret = sol.swapPairs(l1)
print("a")
while ret:
    print(ret.val)
    ret = ret.next

