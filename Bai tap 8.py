class ListNode:
    def __init__(self, value=0, next=None):
        self.value = max(-100, min(value, 100))
        self.next = next

def merge_two_lists(list1, list2):
    list1_length = get_list_length(list1)
    list2_length = get_list_length(list2)
    list1 = truncate_list(list1, 50 - list2_length)
    list2 = truncate_list(list2, 50 - list1_length)

    dummy_head = ListNode()
    current = dummy_head
    
    while list1 and list2:
        if list1.value <= list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    if list1:
        current.next = list1
    elif list2:
        current.next = list2
    
    return dummy_head.next

def get_list_length(head):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
        if length >= 50:
            break
    return length

def truncate_list(head, max_length):
    if not head:
        return None
    current = head
    for _ in range(max_length - 1):
        if current.next:
            current = current.next
        else:
            break
    current.next = None
    return head

def print_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
merged_list = merge_two_lists(list1, list2)
print("Example 1:", print_list(merged_list))

list1 = None
list2 = None
merged_list = merge_two_lists(list1, list2)
print("Example 2:", print_list(merged_list))

list1 = None
list2 = ListNode(0)
merged_list = merge_two_lists(list1, list2)
print("Example 3:", print_list(merged_list))
