class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def remove_elements(head, val):
    while head and head.value == val:
        head = head.next
    current = head
    prev = None
    while current:
        if current.value == val:
            if prev:
                prev.next = current.next
            current = current.next
        else:
            prev = current
            current = current.next
    
    return head

def print_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)
val = 6
head = remove_elements(head, val)
print("Example 1:", print_list(head))

head = None
val = 1
head = remove_elements(head, val)
print("Example 2:", print_list(head))

head = ListNode(7)
head.next = ListNode(7)
head.next.next = ListNode(7)
head.next.next.next = ListNode(7)
val = 7
head = remove_elements(head, val)
print("Example 3:", print_list(head))