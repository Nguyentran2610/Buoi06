class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def print_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
reversed_head = reverse_linked_list(head)
print("Example 1:", print_list(reversed_head))


head = ListNode(1)
head.next = ListNode(2)
reversed_head = reverse_linked_list(head)
print("Example 2:", print_list(reversed_head))

head = None
reversed_head = reverse_linked_list(head)
print("Example 3:", print_list(reversed_head))