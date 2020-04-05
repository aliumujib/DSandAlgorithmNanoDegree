from binary_trees import Node
from stack import Stack
from stack import State
from BFS import Queue

"""
To do at end of ND, visit to deepdive binary_trees some more.

https://www.youtube.com/watch?v=SiyEwLrPpyQ&list=PLeIMaH7i8JDj7DnmO7lll97P1yZjMCpgY
"""


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def compare(self, node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

    def search(self, value):
        """
        implement search
        """
        if self.get_root() is None:
            return False
        else:
            node = self.get_root()
            search_node = Node(value)

            while(node):
                if node.value == search_node.value:
                    return True
                elif self.compare(node, search_node) == -1:
                    if node.has_left_child() and self.compare(node.get_left_child(), search_node) == 0:
                        return True
                    else:
                        node = node.get_left_child()
                elif self.compare(node, search_node) == 1:
                    if node.has_right_child() and self.compare(node.get_right_child(), search_node) == 0:
                        return True
                    else:
                        node = node.get_right_child()
                elif not node.has_left_child() and not node.has_right_child():
                    return False

            return False

    """
    define insert here
    can use a for loop (try one or both ways)
    """

    def insert_with_loop(self, new_value):
        new_node = Node(new_value)
        if self.get_root() is None:
            self.set_root(new_value)
        else:
            node = self.get_root()

            while(True):
                if self.compare(node, new_node) == 0:
                    node.set_value(new_node.value)
                    break
                elif self.compare(node, new_node) == -1:
                    if(node.has_left_child()):
                        node = node.get_left_child()
                    else:
                        node.set_left_child(new_node)
                        break
                elif self.compare(node, new_node) == 1:
                    if(node.has_right_child()):
                        node = node.get_right_child()
                    else:
                        node.set_right_child(new_node)
                        break

    """
    define insert here (can use recursion)
    try one or both ways
    """

    def recursive_insert(self, node, new_node):
        if node:

            if(self.compare(node, new_node) == 0):
                print("{} is equal to {}".format(new_node, node))
                node.value = new_node.value
            elif(self.compare(node, new_node) == -1):
                print("{} is less than {}".format(new_node, node))
                if node.has_left_child():
                    self.recursive_insert(node.get_left_child(), new_node)
                else:
                    node.set_left_child(new_node)
            elif(self.compare(node, new_node) == 1):
                print("{} is greater than {}".format(new_node, node))
                if node.has_right_child():
                    self.recursive_insert(node.get_right_child(), new_node)
                else:
                    node.set_right_child(new_node)
        else:
            print("empty tree")
            self.set_root(new_node.value)

    def insert_with_recursion(self, value):
        starting_node = self.get_root()
        new_node = Node(value)
        self.recursive_insert(starting_node, new_node)

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq((node, level))
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))

            if node.has_right_child():
                q.enq((node.get_right_child(), level + 1))
            else:
                q.enq((None, level + 1))

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s


tree = BinarySearchTree()
tree.insert_with_loop(5)
tree.insert_with_loop(6)
tree.insert_with_loop(4)
tree.insert_with_loop(2)
tree.insert_with_loop(5)  # insert duplicate
print(tree)


tree = BinarySearchTree()
tree.insert_with_recursion(5)
tree.insert_with_recursion(6)
tree.insert_with_recursion(4)
tree.insert_with_recursion(2)
tree.insert_with_recursion(5)  # insert duplicate
print(tree)


tree = BinarySearchTree()
tree.insert_with_recursion(5)
tree.insert_with_recursion(6)
tree.insert_with_recursion(4)
tree.insert_with_recursion(2)

print("search for 8: {} search for 2: {}".format(tree.search(8), tree.search(2)))
print(tree)
