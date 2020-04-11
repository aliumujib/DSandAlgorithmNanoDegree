import hashlib
from datetime import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        assert data is not None

        self.timestamp = timestamp
        self.data = str(data)
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def __repr__(self):
        return "[data: {}\n timestamp: {}\n previoushash: {}\n hash:{}]".format(self.data, self.timestamp,
                                                                                self.previous_hash, self.hash)

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = self.data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class BlockChain:

    def __init__(self):
        self.list = []
        self.current_index = -1

    def get_head_of_chain(self):
        if len(self.list) == 0:
            return None
        else:
            return self.list[0]

    def __str__(self):
        out_string = ""
        for item in self.list:
            out_string += str(item.data) + " -> "

        return out_string

    def prepend(self, value):
        if self.get_head_of_chain() is None:  # perfect, LOL
            node = Block(datetime.now(), value, 0)
            self.list.insert(0, node)
        else:
            last_head = self.get_head_of_chain()
            block = Block(datetime.now(), value, 0)
            last_head.previous_hash = block.hash
            self.list.insert(0, block)
        print("prepended node with hash {}".format(self.get_head_of_chain().hash))

    def append(self, value):
        if self.get_head_of_chain() is None:
            self.list.insert(0, Block(datetime.now(), value, 0))
            print("appended node with hash {}".format(self.get_head_of_chain().hash))
        else:
            last_block = self.list[-1]
            block = Block(datetime.now(), value, last_block.hash)
            self.list.append(block)
            print("appended node with hash {}".format(block.hash))

    def search(self, hash):
        """ Search the BlockChain for a block with the requested value and return the node. """

        if self.get_head_of_chain() is None:
            return None
        else:
            for item in self.list:
                if hash == item.hash:
                    return item
        return None

    def delete(self, value):
        """Block chain nodes cannot be deleted """
        print("Block chain nodes cannot be deleted")
        return None


block_chain_1 = BlockChain()
block_chain_2 = BlockChain()
block_chain_3 = BlockChain()

element_1 = ["If you are not new to programming", "Recursion is a programming pattern",
             "at is useful in situations when a task can be naturally split", "That’s called recursion"]

for ele in element_1:
    block_chain_1.append(ele)

print(block_chain_1)

print(
    "FOUND RESULT: {}".format(block_chain_1.search("3c8e698f72c8b056ed99d8088cc08b376aa6f0f09fbdab2a4366009f90b2a74d")))

print("FOUND RESULT: {}".format(block_chain_1.search("3c8e698f72c8b056ed99d8088cc08b376aa6f0f09fbdab2a4366009f90b24d")))

element_2 = ["For something simple to start with", "that raises x to a natural power of",
             "There are two ways to implement it.", "Recursive thinking: simplify the task"]

for ele in element_2:
    block_chain_2.append(ele)

print(block_chain_2)

element_3 = [None, 0,
             None, -120002]

for ele in element_3:
    block_chain_3.append(ele)

print(element_3)
