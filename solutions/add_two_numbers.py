# 


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.first = None
        self.last = None

    def append(self, node):
        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def __repr__(self):
        r"""convenience function for debugging"""
        s = ''
        current = self.first
        while current is not None:
            s += str(current.val) + '- '
            current = current.next
        return s


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        summed = LinkedList()
        c1 = l1.first
        c2 = l2.first
        carry_over = 0
        while c1 is not None or c2 is not None:
            val = carry_over
            if c1 is not None:
                val += c1.val
                c1 = c1.next
            if c2 is not None:
                val += c2.val
                c2 = c2.next
            if val > 9:
                carry_over = 1
                val = 0
            else:
                carry_over = 0
            summed.append(ListNode(val))
        return summed


if __name__ == '__main__':
    l1 = LinkedList()
    [l1.append(ListNode(x)) for x in (2, 4, 5)]
    l2 = LinkedList()
    [l2.append(ListNode(x)) for x in (5, 6, 4, 5, 7)]
    print(l1)
    print(l2)
    sol = Solution()
    summed_list = sol.addTwoNumbers(l1, l2)
    print(summed_list)
