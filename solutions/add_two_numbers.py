# 


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        current = self
        s = ''
        while current is not None:
            s += str(current.val) + '- '
            current = current.next
        return s


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

    def my_addTwoNumbers(self, l1, l2):
        """
        :type l1: LinkedList
        :type l2: LinkedList
        :rtype: LinkedList
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

    def addTwoNumbers(self, n1, n2, carry_over=0):
        """
        :type n1: ListNode
        :type n2: ListNode
        :rtype: ListNode
        """
        val = sum([n.val for n in (n1, n2) if n is not None]) + carry_over
        carry_over = val // 10
        ret = ListNode(val % 10)
        first = ret
        while (n1 is not None or n2 is not None) or carry_over != 0:
            if n1.next is None:
                n1.next = ListNode(0)
            if n2.next is None:
                n2.next = ListNode(0)
            ret.next = self.addTwoNumbers(n1.next, n2.next, carry_over)
        return first


if __name__ == '__main__':
    l1 = LinkedList()
    [l1.append(ListNode(x)) for x in (2, 4, 5)]
    l2 = LinkedList()
    [l2.append(ListNode(x)) for x in (5, 6, 4, 5, 7)]
    sol = Solution()
    summed_list = sol.my_addTwoNumbers(l1, l2)
    summed_list = sol.addTwoNumbers(l1.first, l2.first)

    l1 = LinkedList()
    [l1.append(ListNode(x)) for x in (2, 4, 5)]
    l2 = LinkedList()
    print('l1 =', l1)
    print('l2 =', l2)
    print(sol.my_addTwoNumbers(l1, l2))
    print(sol.addTwoNumbers(l1.first, l2.first))
