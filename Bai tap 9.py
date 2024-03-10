class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def delete_duplicates(head):
    if not head or not head.next:
        return head
    
    current = head
    while current and current.next:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
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
head.next = ListNode(1)
head.next.next = ListNode(2)
head = delete_duplicates(head)
print("Example 1:", print_list(head))

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)
head = delete_duplicates(head)
print("Example 2:", print_list(head))