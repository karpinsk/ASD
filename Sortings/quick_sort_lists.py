class Node:
    def __init__(self):
        self.next = None
        self.value = None

def qsort(head):
    if head is None:
        return
    if head.next is None:
        return head
    less, eq, great = partition(head)
    """
    print("less:", end=" ")
    printlist(less)
    print("eq:", end=" ")
    printlist(eq)
    print("great:", end=" ")
    printlist(great)
    """
    head = insert_to_end(qsort(less), eq)
    head = insert_to_end(head, qsort(great))
    return head

def partition(head):
    eq = Node()
    less = Node()
    great = Node()
    while head is not None:
        if eq.value is None:
            eq.value = head.value
        elif head.value == eq.value:
            eq = insert_to_begin(eq, head.value)
        elif head.value > eq.value:
            if great.value is None:
                great.value = head.value
            else:
                great = insert_to_begin(great, head.value)
        else:
            if less.value is None:
                less.value = head.value
            else:
                less = insert_to_begin(less, head.value)
        head = head.next
    if less.value is None:
        less = None
    if eq.value is None:
        eq = None
    if great.value is None:
        great = None
    return less, eq, great

def insert_to_begin(head, value):
    node = Node()
    node.value = value
    node.next = head
    head = node
    return head

def insert_to_end(head, node):
    if head is None and node is not None:
        return node
    tmp = head
    while tmp.next is not None:
        tmp = tmp.next
    tmp.next = node
    return head