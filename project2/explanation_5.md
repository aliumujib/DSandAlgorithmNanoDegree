#Blockchain

This was a pretty normal LinkedList implementation except that each Block now had to store a hash of the previous Block,
not a lot changed from how I learnt to implement a LinkedList. I used a python list since it allowed me to easily manage
data in the blockchain and perform operations in constant time.


###Time complexity
- The worst case time complexity for insertion into the LinkedList that is built on a python list is O(1) and the same applied to the blockchain implementation.
- The worst case time for search from the LinkedList is also O(n)  and the same applied to the blockchain implementation.

###Space complexity
- The space complexity for storing the BlockChain is O(n) where n is the number of nodes

---