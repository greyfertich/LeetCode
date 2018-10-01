# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = ""
        num2 = ""
        cur = l1
        num1 += str(cur.val)
        while cur.next:
            cur = cur.next
            num1 += str(cur.val)
        cur = l2
        num2 += str(cur.val)
        while cur.next:
            cur = cur.next
            num2 += str(cur.val)
        ans = str(int(num2[::-1]) + int(num1[::-1]))[::-1]
        out = ListNode(int(ans[0]))
        cur = out
        for i in range(1,len(ans)):
            cur.next = ListNode(int(ans[i]))
            cur = cur.next
        return out
                
