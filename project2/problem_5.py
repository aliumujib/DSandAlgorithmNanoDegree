import hashlib
from datetime import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def __repr__(self):
        return "[{} {} {} {}]".format(self.data, self.timestamp, self.previous_hash, self.hash)

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = self.data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class BlockChain:

    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def prepend(self, value):
        if self.head is None:  # perfect
            self.head = Block(datetime.now(), value, 0)
        else:
            node = Block(datetime.now(), value, 0)
            self.head.previous_hash = node.hash
            node.next = self.head
            self.head = node

    def append(self, value):
        if self.head is None:
            self.head = Block(datetime.now(), value, 0)
        else:
            traverser = self.head
            while traverser.next:
                traverser = traverser.next
            traverser.next = Block(datetime.now(), value, traverser.hash)

    def search(self, value):
        """ Search the BlockChain for a block with the requested value and return the node. """

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

    def delete(self, value):
        """ Search the BlockChain for a block with the requested value and return the node. """

        if self.head is None:
            return None
        else:
            traverser = self.head
            previous = None
            while traverser.next:
                if traverser.value == value:
                    next_val = traverser.next
                    previous.next = next_val
                    next_val.previous_hash = previous.hash
                    return traverser
                else:
                    previous = traverser
                    traverser = traverser.next
        return None


block_chain_1 = BlockChain()
block_chain_2 = BlockChain()

element_1 = ["If you are not new to programming", "Recursion is a programming pattern",
             "at is useful in situations when a task can be naturally split", "That’s called recursion"]

for ele in element_1:
    block_chain_1.append(ele)

print(block_chain_1)

element_2 = ["For something simple to start with", "that raises x to a natural power of",
             "There are two ways to implement it.", "Recursive thinking: simplify the task"]

for ele in element_2:
    block_chain_2.append(ele)

print(block_chain_2)
