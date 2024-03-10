class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    def remove_duplicates(self):
        if self.head is None:
            return
        
        seen_values = set()
        prev_node = None
        current_node = self.head
        
        while current_node is not None:
            if current_node.value in seen_values:
                prev_node.next = current_node.next
            else:
                seen_values.add(current_node.value)
                prev_node = current_node
            current_node = current_node.next
        
        self.length = len(seen_values)

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)
linked_list.append(3)
linked_list.append(4)
linked_list.append(2)
print(linked_list)
linked_list.remove_duplicates()
print(linked_list)
