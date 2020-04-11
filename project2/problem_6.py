class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def __add_ll_to_set__(node, set):
    if node:
        set.add(node.value)
        node = node.next
        return __add_ll_to_set__(node, set)
    else:
        return set


def __make_ll_from_set__(set):
    ll = LinkedList()
    for item in set:
        ll.append(item)
    return ll


def union(llist_1, llist_2):
    union_set = __add_ll_to_set__(llist_1.head, set())
    union_set = __add_ll_to_set__(llist_2.head, union_set)
    return __make_ll_from_set__(union_set)


def intersection(llist_1, llist_2):
    intersection_set1 = __add_ll_to_set__(llist_1.head, set())
    intersection_set2 = __add_ll_to_set__(llist_2.head, set())

    intersection_set = intersection_set1.intersection(intersection_set2)

    return __make_ll_from_set__(intersection_set)


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("UNION: {}".format(union(linked_list_1, linked_list_2)))
print("INTERSECTION: {}".format(intersection(linked_list_1, linked_list_2)))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("UNION: {}".format(union(linked_list_3, linked_list_4)))
print("INTERSECTION: {}".format(intersection(linked_list_3, linked_list_4)))



# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [None, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, "7", 8, 9, "11", 21, 1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print("UNION: {}".format(union(linked_list_5, linked_list_6)))
print("INTERSECTION: {}".format(intersection(linked_list_5, linked_list_6)))
