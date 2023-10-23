from math import log2, ceil
from data_structures.simply_linked_list import SimplyLinkedList


# Q6
def ten_biggest_numbers(list):
    if len(list) < 10:
        return list
    biggests = []
    biggest = index_biggest = index = 0
    for _ in range(10):
        while index < len(list):
            if list[index] > biggest:
                biggest = list[index]
                index_biggest = index
            index += 1
        biggests.append(list.pop(index_biggest))
        biggest = index = 0
    return biggests


# Q7
def find_poisoned_bottle(bottles):
    n = len(bottles)
    p = ceil(log2(n + 1))
    poisoned = []
    for num, bottle in enumerate(bottles):
        if bottle == 1:
            poisoned_bottle = bin(num + 1)[2:]
            print(f'Garrafa envenenada: {num + 1}')
            for i in range(len(poisoned_bottle) - 1, -1, -1):
                if int(poisoned_bottle[len(poisoned_bottle) - i - 1]) == 1:
                    poisoned.insert(0, i + 1)
            print(f'Dentre os {p} provadores, foram envenenados: {poisoned}')


# Q8
def biggest_number(list, biggest=0, index=0):
    if len(list) == 0:
        return None
    elif len(list) == 1:
        return list[0]
    elif index == len(list):
        return biggest
    else:
        if list[index] > biggest:
            biggest = list[index]
        return biggest_number(list, biggest, index + 1)


# Q10
def move_even_number_to_beginning(list, index=0, count=0):
    if len(list) <= 1 or count == len(list):
        return list
    if list[index] % 2:
        list.append(list.pop(index))
        return move_even_number_to_beginning(list, index, count + 1)
    return move_even_number_to_beginning(list, index + 1, count + 1)


# Q12
def remove_even_numbers(linked_list):
    if linked_list.is_empty():
        return None
    current = previous = linked_list.head
    while current:
        if current.data % 2 == 0:
            if current == linked_list.head:
                linked_list.head = current.next
                current = previous = linked_list.head
            previous.next = current.next
        else:
            previous = current
        current = current.next
    return linked_list


# Q13
def sum_odd_numbers(linked_list):
    if linked_list.is_empty():
        return None
    sum = 0
    current = linked_list.head
    while current:
        if current.data % 2:
            sum += current.data
        current = current.next
    return sum


# Q14
def split_linked_list(linked_list):
    if linked_list.size <= 1:
        return None
    lc1 = SimplyLinkedList()
    lc2 = SimplyLinkedList()
    lc1.size = linked_list.size // 2
    current = lc1.head = linked_list.head
    for _ in range(lc1.size - 1):
        current = current.next
    lc2.head = current.next
    lc2.size = linked_list.size - lc1.size
    current.next = lc1.head
    current = lc2.head
    for _ in range(lc2.size - 1):
        current = current.next
    current.next = lc2.head
    print(lc1)
    print(lc2)


# Q15
def interlace_linked_lists(ll1, ll2):
    ll3 = SimplyLinkedList()
    current_ll1 = ll1.head
    current_ll2 = ll2.head
    while current_ll1 and current_ll2:
        ll3.insert_at_end(current_ll1.data)
        ll3.insert_at_end(current_ll2.data)
        current_ll1 = current_ll1.next
        current_ll2 = current_ll2.next
    if ll1.size > ll2.size:
        while current_ll1:
            ll3.insert_at_end(current_ll1.data)
            current_ll1 = current_ll1.next
    elif ll1.size < ll2.size:
        while current_ll2:
            ll3.insert_at_end(current_ll2.data)
            current_ll2 = current_ll2.next
    return ll3
