# Let's define a stack to help keep track of the tree nodes
from binary_trees import Tree
from binary_trees import Node
from stack import Stack
from stack import State

root_node = Node("Apples")
root_node.set_left_child(Node("Oranges"))
root_node.set_right_child(Node("Agbalumo"))
root_node.get_left_child().set_right_child(Node("Berries"))
root_node.get_left_child().set_left_child(Node("Mangoes"))
root_node.get_right_child().set_right_child(Node("Cashews"))

fruit_tree = Tree(root_node)
stack = Stack()


def recursive_traverse_tree_dfs_pre_order(node, traversal_order):
    if node:
        traversal_order.append(node.value)
        recursive_traverse_tree_dfs_pre_order(node.get_left_child(), traversal_order)
        recursive_traverse_tree_dfs_pre_order(node.get_right_child(), traversal_order)
    return traversal_order


print(recursive_traverse_tree_dfs_pre_order(fruit_tree.get_root_node(), list()))


def recursive_traverse_tree_dfs_in_order(node, traversal_order):
    if node:
        recursive_traverse_tree_dfs_in_order(node.get_left_child(), traversal_order)
        traversal_order.append(node.value)
        recursive_traverse_tree_dfs_in_order(node.get_right_child(), traversal_order)
    return traversal_order


print(recursive_traverse_tree_dfs_in_order(fruit_tree.get_root_node(), list()))


def recursive_traverse_tree_dfs_post_order(node, traversal_order):
    if node:
        recursive_traverse_tree_dfs_post_order(node.get_left_child(), traversal_order)
        recursive_traverse_tree_dfs_post_order(node.get_right_child(), traversal_order)
        traversal_order.append(node.value)
    return traversal_order


print(recursive_traverse_tree_dfs_post_order(fruit_tree.get_root_node(), list()))
