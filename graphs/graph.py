class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)

    def __repr__(self):
        return "{}".format(self.value)


class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)


nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS, nodeH, nodeG, nodeP, nodeR, nodeA])
graph1.add_edge(nodeG, nodeR)
graph1.add_edge(nodeA, nodeR)
graph1.add_edge(nodeA, nodeG)
graph1.add_edge(nodeR, nodeP)
graph1.add_edge(nodeH, nodeG)
graph1.add_edge(nodeH, nodeP)
graph1.add_edge(nodeS, nodeR)


def dfs_walk_iterative(root_node):
    visited_nodes = []
    stack = [root_node]

    while len(stack) > 0:
        current_node = stack.pop()
        visited_nodes.append(current_node)

        for child in current_node.children:
            if child not in visited_nodes and child not in stack:
                stack.append(child)
    return visited_nodes


def dfs_walk_recursive(stack, results):
    if len(stack) == 0:
        return results
    else:
        current_node = stack.pop()
        results.append(current_node)
        if len(current_node.children) > 0:
            for child in current_node.children:
                if child not in stack and child not in results:
                    stack.append(child)

        return dfs_walk_recursive(stack, results)


def dfs_search_recursive(node, visited, target):
    if not node:
        return
    elif node.value == target:
        return node
    else:
        visited.append(node.value)
        for child in node.children:
            if child.value not in visited:
                return dfs_search_recursive(child, visited, target)


def dfs_search_iterative(root_node, target):
    visited_nodes = []
    stack = [root_node]

    while len(stack) > 0:
        current_node = stack.pop()
        visited_nodes.append(current_node)

        if current_node.value == target:
            return current_node

        for child in current_node.children:
            if child not in visited_nodes and child not in stack:
                stack.append(child)
    return None


print("Iterative {}".format(dfs_walk_iterative(nodeG)))
print("Search iterative {}".format(dfs_search_iterative(nodeG, "A")))

print("Recursive {}".format(dfs_walk_recursive([nodeG], [])))
print("Search recursive {}".format(dfs_search_recursive(nodeG, [], "A")))
