class Heap:
    def __init__(self, initial_size):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go

    def insert(self, data):
        """
        Insert `data` into the heap
        """
        last_idx = self.next_index
        if self.next_index >= len(self.cbt) - 1:
            self.__double_cbt_array_size__()
        self.cbt[self.next_index] = data
        self.up_heapify(self.next_index)
        # print('Current heap is after addition: {}'.format(self.cbt))
        self.next_index = self.next_index + 1
        # self.next_index = self.calc_next_child_idx(self.calc_parent_idx(self.next_index))

        # print("INSERTED: {} at {}, next Idx is {}".format(data, last_idx, self.next_index))

    def remove(self):
        """
        Remove and return the element at the top of the heap
        """
        top_element = self.cbt[0]
        last_element = self.cbt[self.next_index - 1]

        self.cbt[self.next_index - 1] = None
        self.cbt[0] = last_element
        if self.next_index > 0:
            self.next_index = self.next_index - 1
        self.down_heapify(0)

        # print('Current heap after removal is: {}'.format(self.cbt))
        return top_element

    def down_heapify(self, index):
        if self.cbt[index] is not None and self.cbt[index+1] is not None and self.cbt[index] > self.cbt[index + 1]:
            root_element = self.cbt[index]
            leaf_element = self.cbt[index + 1]
            # print("Down Heapifying for {} , {}".format(root_element, leaf_element))
            self.cbt[index] = leaf_element
            self.cbt[index + 1] = root_element
            self.down_heapify(index + 1)

    def up_heapify(self, idx):
        parent_idx = self.calc_parent_idx(idx)
        # print("Parent index for {} is {}".format(idx, parent_idx))
        if self.cbt[parent_idx] is not None and self.cbt[parent_idx] > self.cbt[idx]:
            # print("Up Heapifying for {} , {}".format(self.cbt[parent_idx], self.cbt[idx]))
            temp = self.cbt[parent_idx]
            self.cbt[parent_idx] = self.cbt[idx]
            self.cbt[idx] = temp
            self.up_heapify(parent_idx)

    def size(self):
        return self.next_index

    def get_minimum(self):
        return self.cbt[0]

    def is_empty(self):
        return self.next_index == 0

    def calc_next_child_idx(self, idx):
        if ((2 * idx) + 1 >= len(self.cbt) - 1) or ((2 * idx) + 2 >= len(self.cbt) - 1):
            self.__double_cbt_array_size__()

        if self.cbt[(2 * idx) + 1] is None:
            return (2 * idx) + 1
        elif self.cbt[(2 * idx) + 2] is None:
            return (2 * idx) + 2
        else:
            return self.calc_next_child_idx((2 * idx) + 1)

    @staticmethod
    def calc_parent_idx(idx):
        return (idx - 1) // 2

    def __repr__(self):
        return "{}".format(self.cbt)

    def __double_cbt_array_size__(self):
        print("Increasing array size")
        new_cbt = [None for _ in range(2 * len(self.cbt))]
        for index, each in enumerate(self.cbt):
            new_cbt[index] = each

        self.cbt = new_cbt


heap_size = 5
heap = Heap(heap_size)

elements = [1, 2, 3, 4, 1, 2]
for element in elements:
    heap.insert(element)
print('Inserted elements: {}'.format(elements))

print('size of heap: {}'.format(heap.size()))

for _ in range(4):
    print('Call remove: {}'.format(heap.remove()))

print('Call get_minimum: {}'.format(heap.get_minimum()))

for _ in range(2):
    print('Call remove: {}'.format(heap.remove()))

print('size of heap: {}'.format(heap.size()))
print('Call remove: {}'.format(heap.remove()))
print('Call is_empty: {}'.format(heap.is_empty()))