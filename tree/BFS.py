from binary_trees import Tree
from binary_trees import Node
from stack import Stack
from stack import State

from collections import deque


class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


root_node = Node("Apples")
root_node.set_left_child(Node("Oranges"))
root_node.set_right_child(Node("Agbalumo"))
root_node.get_left_child().set_right_child(Node("Berries"))
root_node.get_left_child().set_left_child(Node("Mangoes"))
root_node.get_right_child().set_right_child(Node("Cashews"))

fruit_tree = Tree(root_node)
stack = Stack()


def bfs_traverser(tree):
    queue = Queue()
    visit_order = list()

    node = tree.get_root_node()
    queue.enq(node)

    while len(queue) > 0:
        node = queue.deq()

        visit_order.append(node)

        if node.has_left_child():
            queue.enq(node.get_left_child())
        if node.has_right_child():
            queue.enq(node.get_right_child())

    return visit_order


def print_tree(tree):
    queue = Queue()
    visit_order = list()
    level = 0
    node = tree.get_root_node()
    queue.enq((node, level))

    while len(queue) > 0:
        node, level = queue.deq()

        if node == None:
            visit_order.append(('<empty>', level))
            continue

        visit_order.append((node, level))

        if node.has_left_child():
            queue.enq((node.get_left_child(), level + 1))
        else:
            queue.enq((None, level + 1))
        if node.has_right_child():
            queue.enq((node.get_right_child(), level + 1))
        else:
            queue.enq((None, level + 1))

    last_printed_level = -1
    string = ""
    for i in range(len(visit_order)):

        node, current_lvl = visit_order[i]

        if(last_printed_level < current_lvl):
            string = string + "{}|{}\n".format(node.get_left_child(), node.get_right_child())
        else:
            string = string + "{} | {}\t".format(node.get_left_child(), node.get_right_child())

        # print(string)
    return string


# print(print_tree(fruit_tree))
