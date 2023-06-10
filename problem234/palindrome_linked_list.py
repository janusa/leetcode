def is_palindrome(head):
    # Find length of singly linked list
    linked_list_length = 0
    node = head
    while node is not None:
        linked_list_length += 1
        node = node.next

    half_length = linked_list_length / 2  # Python3, otherwise divide by 2.0

    # Find middle node if odd number of nodes, otherwise find the first one of the two middles ones
    i = 0
    node = head
    while i < half_length - 1:
        node = node.next
        i += 1

    middle_node = node

    # Reverse second half of the linked list.
    # If odd number of nodes, reverse all nodes after middle, otherwise reverse all nodes from the second middle node
    previous_node = None
    current_node = node.next
    next_node = node.next
    while current_node is not None:
        next_node = next_node.next
        current_node.next = previous_node

        previous_node = current_node
        current_node = next_node

    middle_node.next = previous_node

    # Verify if linked list is palindrome
    reversed_current = previous_node
    current = head
    while reversed_current is not None:
        if current.val != reversed_current.val:
            return False
        current = current.next
        reversed_current = reversed_current.next
    return True
