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
        num1 = []
        num2 = []
        current = l1
        while True:
            num1.append(current.val)
            if current.next == None:
                break
            current = current.next
        current = l2
        while True:
            num2.append(current.val)
            if current.next == None:
                break
            current = current.next
        num1 = list(reversed(num1))
        num2 = list(reversed(num2))
        st1 = ''
        st2 = ''
        for i in num1:
            st1 += str(i)
        for i in num2:
            st2 += str(i)
        new = list(str(int(st1) + int(st2)))
        new.reverse()
        link = ListNode(int(new[0]))
        current = link
        for i in range(len(new)):
            if i > 0:
                current.next = ListNode(int(new[i]))
                current = current.next
        return link
                
