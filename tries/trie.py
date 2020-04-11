class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

    def __repr__(self):
        return "{} is_word: {}".format(self.children, self.is_word)


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """
        last_node = self.root
        for index, character in enumerate(word):
            node = TrieNode()

            if character not in last_node.children:
                last_node.children[character] = node
                if index == len(word) - 1:
                    node.is_word = True

            last_node = last_node.children[character]

    def exists(self, word):
        """
        Check if word exists in trie
        """
        last_node = self.root
        for index, character in enumerate(word):

            if character in last_node.children:

                if index == len(word) - 1:
                    return last_node.children[character].is_word

                last_node = last_node.children[character]
                print("{} : {}\n".format(character, last_node))


word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses', 'zebra']
word_trie = Trie()

# Add words
for word in word_list:
    word_trie.add(word)

print(word_trie.root)

# Test words
test_words = ['bear', 'goo', 'good', 'goos']
for word in test_words:
    if word_trie.exists(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))
