# Intersection of Two Linked Lists

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# hash table, faster than 11.55% 
class Solution1(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """ 
        if headA == None or headB == None:
            return None
        
        dic = {}
        while headA:
            dic[headA] = headA.next
            headA = headA.next
        
        while headB:
            if headB in dic and dic[headB] == headB.next:
                return headB
            else:
                headB = headB.next
        
        return None


# start from intersect node to the end node, two lists are same
# find the same length of two lists, and then iterate
# faster than 91.55%
class Solution2(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        
        pa, pb = headA, headB
        lena, lenb = 0, 0
        while pa:
            lena += 1
            pa = pa.next
            
        while pb:
            lenb += 1
            pb = pb.next
        
        if lena > lenb:
            gap = lena - lenb
            while gap:
                headA = headA.next
                gap -= 1
            while lenb:
                if headA == headB:
                    return headA
                else:
                    headA = headA.next
                    headB = headB.next
                    lenb -= 1
            return None
        elif lena < lenb:
            gap = lenb - lena
            while gap:
                headB = headB.next
                gap -= 1
            while lenb:
                if headA == headB:
                    return headA
                else:
                    headA = headA.next
                    headB = headB.next
                    lenb -= 1
            return None
        else:
            while lena:
                if headA == headB:
                    return headA
                else:
                    headA = headA.next
                    headB = headB.next
                    lena -= 1
            return None


# two points
# faster than 42.43% 
class Solution3(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None

        pa = headA
        pb = headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa