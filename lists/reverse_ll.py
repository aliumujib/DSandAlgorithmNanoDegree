# Helper Code


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])

        def prepend(linked_list, val):
            if linked_list.head is None:
                linked_list.head = Node(val)
                return
            head = linked_list.head
            node = Node(val)
            node.next = head
            linked_list.head = node

        def reverse(linked_list):
            """
            Reverse the inputted linked list

            Args:
               linked_list(obj): Linked List to be reversed
            Returns:
               obj: Reveresed Linked List
            """

            new_linked_list = LinkedList()
            traverser = linked_list.head

            while traverser:
                prepend(new_linked_list, traverser.value)
                traverser = traverser.next

            return new_linked_list


llist = LinkedList()
for value in [4, 2, 5, 1, -3, 0]:
llist.append(value)

flipped = reverse(llist)
print(flipped)
is_correct = list(flipped) == list([0, -3, 1, 5, 2, 4]) and list(llist) == list(reverse(flipped))
print("Pass" if is_correct else "Fail")
