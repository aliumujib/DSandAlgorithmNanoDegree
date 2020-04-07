#Huffman Coding

This was by far the most interesting part of the assignment, I had to do some research on Youtube as I had never come accross Huffman coding before,
the video at https://www.youtube.com/watch?v=JsTptu56GM8&t=268s was particularly useful. I had an idea to use a deque from the collections package as a
means of storing nodes and then sorting the queue on each pass but fortunately I read enough to come across the heapq class which made things a lot easier to 
manage. I don't think it helped time complexity a lot but  I am of the opinion that compression is basically trading time for more space. 

####Encoding
I approached a solution to the problem by breaking the problem down into chunks:
- First I used a HashMap to collate the frequency of each character.
- From the frequency I built a tree of nodes by constantly popping 2 of the lowest frequencies from the heap, adding them together and pushing the results back onto 
the heap. I found and fixed a very funny bug that I detailed in my comment on the __build_tree__() method.
- I also spent sometime looking for a way to pretty print the tree generated. Ended up using some code from https://stackoverflow.com/a/54074933/4612737 (still trying to completely figure out how it does its thing).
- By traversing the tree (depth-first pre-order traversal) I built a key_code_map_ that stored codes and their corresponding characters.
- Using the key_code_map, I encoded the string and returned the result as a tuple.

####Decoding
- This was a simpler step, I basically kept recursively tracing the input string on the tree and recording characters that I found at the root nodes.

###Time complexity
- The time complexity for encoding is O(n) because the worst case time complexity for all operations in a BST is O(n), the loop for building the hashmap of character frequencies also has time complexity of O(n)
- The time complexity for decoding from the compressed string is also O(n log k) where k is the number of nodes because it takes O(log k) node visits to decode each symbol and the number of inputs reduces after each symbol is found.

###Space complexity
- The space complexity is O(k) for the tree where K is the number of nodes and O(n) for the encoded string where n is the number of characters in the encoded string.
 

---