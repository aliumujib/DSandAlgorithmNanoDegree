class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        if self.head is None:  # perfect
            self.head = Node(value)
        else:
            node = Node(value)
            node.next = self.head
            self.head = node

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            traverser = self.head
            while traverser.next:
                traverser = traverser.next
            traverser.next = Node(value)

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """

        if self.head is None:
            return None
        else:
            traverser = self.head
            while traverser.next:
                if traverser.value == value:
                    return traverser
                else:
                    traverser = traverser.next
        return None

    def remove(self, value):
        """ Remove first occurrence of value. """

        if self.head is None:
            return
        elif self.head.value == value:
            self.head = self.head.next
        else:
            traverser = self.head
            previous = None
            while traverser:
                if traverser.value == value:
                    previous.next = traverser.next
                    return
                else:
                    previous = traverser
                    traverser = traverser.next
        return

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        node = self.head
        self.head = self.head.next
        return node.value

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """

        counter = 0
        if pos == 0:
            self.prepend(value)
            return
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node:
            if counter == (pos - 1):
                previous_next = node.next
                data = Node(value)
                node.next = data
                data.next = previous_next
                return
            else:
                if node.next is None:
                    node.next = Node(value)
                    return
                node = node.next
            counter = counter+1

    def size(self):
        """ Return the size or length of the linked list. """

        size = 0
        if self.head == None:
            return size
        if self.head.next == None:
            return 1

        traverser = self.head
        while traverser:
            size = size + 1
            traverser = traverser.next
        return size

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], "list contents: {}".format(linked_list.to_list())
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], "list contents: {}".format(linked_list.to_list())

# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], "list contents: {}".format(linked_list.to_list())
linked_list.append(3)
assert linked_list.to_list() == [1, 3], "list contents: {}".format(linked_list.to_list())

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, "list contents: {}".format(linked_list.to_list())
assert linked_list.search(4).value == 4, "list contents: {}".format(linked_list.to_list())

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], "list contents: {}".format(linked_list.to_list())
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], "list contents: {}".format(linked_list.to_list())
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], "list contents: {}".format(linked_list.to_list())

# Test pop
value = linked_list.pop()
assert value == 2, "list contents: {}".format(linked_list.to_list())
assert linked_list.head.value == 1, "list contents: {}".format(linked_list.to_list())

# Test insert
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], "list contents: {}".format(linked_list.to_list())
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], "list contents: {}".format(linked_list.to_list())
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], "list contents: {}".format(linked_list.to_list())

# Test size
assert linked_list.size() == 5, "list contents: {}".format(linked_list.to_list())
print("list {}".format(linked_list.to_list()))
print("list size {}".format(linked_list.size()))
