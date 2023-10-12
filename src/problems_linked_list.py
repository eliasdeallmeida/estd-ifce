from data_structures.simply_linked_list import SimplyLinkedList


# Slide 28-29
def get_nth_element(linked_list, n):
    if n < 0 or n >= len(linked_list):
        raise IndexError('Invalid index given.')
    element = linked_list.head
    for _ in range(n):
        element = element.next
    return element.data


# Slide 32-33
def remove_elements_by_value(linked_list, value):
    current = linked_list.head
    previous = None
    while current:
        if current.data == value:
            if previous == None:
                linked_list.head = current.next
            else:
                previous.next = current.next
            linked_list.size -= 1
        else:
            previous = current
        current = current.next


# Slide 34-37
def has_cycle(circular_linked_list):
    pass


# Slide 38
def find_middle(linked_list):
    pointer = linked_list.head
    if len(linked_list) % 2:
        for _ in range(len(linked_list) // 2):
            pointer = pointer.next
        return pointer.data
    else:
        for _ in range(len(linked_list) // 2 - 1):
            pointer = pointer.next
        return [pointer.data, pointer.next.data]


# Slide 39
def reverse_linked_list(linked_list):
    if len(linked_list) <= 1:
        return
    current = linked_list.head
    previous = None
    while current.next:
        next = current.next
        current.next = previous
        previous = current
        current = next
    current.next = previous
    linked_list.head = current


# Slide 40
def reverse_in_pairs(linked_list):
    current = linked_list.head
    while current and current.next:
        current_copy = current.data
        current.data = current.next.data
        current.next.data = current_copy
        current = current.next.next


# Slide 41
def remove_repetitions(linked_list):
    current = linked_list.head
    while current.next:
        if current.data == current.next.data:
            current.next = current.next.next
            linked_list.size -= 1
        else:
            current = current.next


# Slide 42
def reverse_at_given_element(current):
    reverse_list = SimplyLinkedList()
    while current:
        reverse_list.insert_at_beginning(current.data)
        current = current.next
    return reverse_list.head


def is_palindrome(linked_list):
    if len(linked_list) == 0:
        return False
    if len(linked_list) == 1:
        return True
    current = first_half = linked_list.head
    for _ in range(linked_list.size // 2):
        current = current.next
    if linked_list.size % 2:
        second_half = reverse_at_given_element(current.next)
    else:
        second_half = reverse_at_given_element(current)
    while second_half:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next
    return True
