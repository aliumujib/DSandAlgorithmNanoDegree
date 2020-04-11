import heapq


class HeapNode:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def __repr__(self):
        s = "{}".format(self.value)
        return s

    def __le__(self, other):
        le = self.value[1] <= other.value[1]
        return le

    def __lt__(self, other):
        lt = self.value[1] < other.value[1]
        return lt

    def __gt__(self, other):
        gt = self.value[1] > other.value[1]
        return gt

    def __cmp__(self, other):
        if other is None:
            return -1
        if not isinstance(other, HeapNode):
            return -1
        return self.value[1] > other.value[1]

    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = "{}".format(self.value)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = "{}".format(self.value)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = "{}".format(self.value)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = "{}".format(self.value)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


# define a Tree class here
class Tree:

    def __init__(self, root):
        self.root = root

    def get_root_node(self):
        return self.root


class HuffmanCoding:

    # An interesting thing I learnt here is comparisons, I started out with a generic node that took tuples but
    # didn't account for how they will be compared while being used on the heap i.e no impl for _lt_ so the heap kept
    # returning items at the front of the list. I also learnt about heaps which are a better alternative that the queue
    # that I had to keep sorting in my first implementation.
    def __build_tree__(self, chars_freq):
        if len(chars_freq) == 1:
            last_node = heapq.heappop(chars_freq)
            return Tree(last_node)
        else:
            item_1 = heapq.heappop(chars_freq)
            item_2 = heapq.heappop(chars_freq)
            # $& special character to mark none root tuples
            parent = HeapNode(("$&", item_1.value[1] + item_2.value[1]))
            parent.set_left_child(item_1)
            parent.set_right_child(item_2)
            heapq.heappush(chars_freq, parent)
            return self.__build_tree__(chars_freq)

    def __make_map_of_key_codes__(self, current_string, result_map, node):
        if not node.left and not node.right:
            result_map[node.value[0]] = current_string
        else:
            self.__make_map_of_key_codes__("{}{}".format(current_string, "0"), result_map, node.left)
            self.__make_map_of_key_codes__("{}{}".format(current_string, "1"), result_map, node.right)

    def __encode_data_using_map__(self, data, result, map):
        if len(data) == 0:
            return result
        else:
            result = result + map[data[0]]
            return self.__encode_data_using_map__(data[1:], result, map)

    def huffman_encoding(self, data):
        if not data:
            return None, None, None
        character_frequencies = self.__count_character_frequencies__(data)
        # print("type {}".format(type(character_frequencies)))
        huffman_tree_ = self.__build_tree__(character_frequencies)
        huffman_tree_.get_root_node().display()
        key_code_map_ = {}
        self.__make_map_of_key_codes__("", key_code_map_, huffman_tree_.get_root_node())
        print(key_code_map_)
        encoded_string_ = self.__encode_data_using_map__(data, "", key_code_map_)
        # print("{}".format(encoded_string_))
        return huffman_tree_, key_code_map_, encoded_string_

    def huffman_decoding(self, data, tree):
        if data is None or tree is None:
            return None
        return self.__decode_data_using_tree__("", data, tree, tree.get_root_node())

    def __decode_data_using_tree__(self, result, data, tree, node):
        if len(data) > 0:
            if node.left and node.right:
                if data[0] == '0':
                    return self.__decode_data_using_tree__(result, data[1:], tree, node.left)
                elif data[0] == '1':
                    return self.__decode_data_using_tree__(result, data[1:], tree, node.right)
            else:
                result = "{}{}".format(result, node.value[0])
                node = tree.get_root_node()
                return self.__decode_data_using_tree__(result, data[0:], tree, node)
        else:
            result = "{}{}".format(result, node.value[0])
            print("RETURNING {}".format(result))
            return result

    @staticmethod
    def __count_character_frequencies__(string):
        map_of_frequencies = {}

        for character in string:
            if character in map_of_frequencies:
                map_of_frequencies[character] = map_of_frequencies[character] + 1
            else:
                map_of_frequencies[character] = 1

        list_of_frequencies = [HeapNode(item) for item in sorted(map_of_frequencies.items(),
                                                                 key=lambda item: item[1])]

        return list_of_frequencies


huffmanCoding = HuffmanCoding()
huffman_tree, key_code_map, encoded_string = huffmanCoding.huffman_encoding(
    "only to get a representation of a dictionary that is sorted. Dictionaries are inherently orderless")
print("DECODED VALUE {} FROM {}".format(huffmanCoding.huffman_decoding(encoded_string, huffman_tree), encoded_string))

huffmanCoding2 = HuffmanCoding()
huffman_tree2, key_code_map2, encoded_string2 = huffmanCoding2.huffman_encoding(
    "- First I used a HashMap to collate the frequency of each character")
print(
    "DECODED VALUE {} FROM {}".format(huffmanCoding.huffman_decoding(encoded_string2, huffman_tree2), encoded_string2))

huffmanCoding3 = HuffmanCoding()
huffman_tree3, key_code_map3, encoded_string3 = huffmanCoding2.huffman_encoding(
    "10000111111")
print(
    "DECODED VALUE {} FROM {}".format(huffmanCoding.huffman_decoding(encoded_string3, huffman_tree3), encoded_string3))

huffmanCoding4 = HuffmanCoding()
huffman_tree4, key_code_map4, encoded_string4 = huffmanCoding2.huffman_encoding(
    None)
print(
    "DECODED VALUE {} FROM {}".format(huffmanCoding.huffman_decoding(encoded_string4, huffman_tree4), encoded_string4))
