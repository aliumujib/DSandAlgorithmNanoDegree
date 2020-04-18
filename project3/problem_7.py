# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode()

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        sub_paths = path.split("/")
        sub_paths = list(filter(lambda a: a != '', sub_paths))
        current_node = self.root
        for index, sub_path in enumerate(sub_paths):
            if index != len(sub_paths) - 1:
                current_node.insert(sub_path, None)
            else:
                current_node.insert(sub_path, handler)

            current_node = current_node.children[sub_path]

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        sub_paths = path.split("/")
        sub_paths = list(filter(lambda a: a != '', sub_paths))
        current_node = self.root
        for sub_path in sub_paths:
            if sub_path in current_node.children:
                current_node = current_node.children[sub_path]
            else:
                return None

        return current_node


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        self.path = None
        self.handler = None
        self.children = {}

    def insert(self, sub_path, handler):
        # Insert the node as before
        if sub_path not in self.children:
            node = RouteTrieNode()
            node.path = sub_path
            node.handler = handler
            self.children[sub_path] = node

    def __repr__(self):
        return "{} {} \t".format(self.children, self.handler)


class Router:

    def __init__(self, root_handler, not_found_handler):
        self.root_handler = root_handler
        self.not_found_handler = not_found_handler
        self.trie = RouteTrie()

    def add_handler(self, path, handler):
        self.trie.insert(path, handler)

    def lookup(self, path):
        node = self.trie.find(path)
        handler = None

        if node:
            handler = node.handler

        if handler:
            return handler
        else:
            return self.not_found_handler


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should pri

router.add_handler("/home/about/me", "me handler")  # add a route
print(router.lookup("/home/about/me"))

# test about handler still works after adding a new sub path
print(router.lookup("/home/about"))
