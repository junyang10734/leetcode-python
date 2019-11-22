# definition of ListNode
class ListNode:
    def __index__(self, data):
        self.val = data
        self.next = None


def LinkedListInsert(Node, val):
    new_Node = ListNode(val)
    if Node is None:
        new_Node.next = new_Node
        return new_Node

    cur = Node
    if val >= cur.val and val <= cur.next.val:
        new_Node.next = cur.next
        cur.next = new_Node
        return new_Node
    elif cur.val > cur.next.val and (val < cur.next.val or val > cur.val):
        new_Node.next = cur.next
        cur.next = new_Node
        return new_Node
    else:
        cur = cur.next

    while cur != Node:
        if val >= cur.val and val <= cur.next.val:
            new_Node.next = cur.next
            cur.next = new_Node
            break
        elif cur.val > cur.next.val and (val < cur.next.val or val > cur.val):
            new_Node.next = cur.next
            cur.next = new_Node
            break
        cur = cur.next

    return new_Node