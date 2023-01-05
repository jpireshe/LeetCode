# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Num = 0
        cases = 0

        while l1:
            l1Num += l1.val * 10**cases
            cases += 1
            l1 = l1.next

        cases = 0
        l2Num = 0

        while l2:
            l2Num += l2.val * 10**cases
            cases += 1
            l2 = l2.next

        retStr = str(l1Num + l2Num)
        retStr = retStr[::-1]

        # build a linked list w that
        ret = ListNode(int(retStr[0]), None)
        retCurr = ret
        
        if len(retStr) == 1: return ret
        for i in range(1, len(retStr)):
            retCurr.next = ListNode(int(retStr[i]), None)
            retCurr = retCurr.next

        return ret