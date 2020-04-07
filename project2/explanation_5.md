#Blockchain

This was a pretty normal LinkedList implementation except that each Block now had to store a hash of the previous Block,
not a lot changed from how I learnt to implement a LinkedList except for `deletions` where I now had to update the previous
hash for the replacement of the deleted block. 


###Time complexity
- The worst case time complexity for insertion into the LinkedList is O(n) and the same applied to the blockchain implementation.
- The worst case time complexity for deletion from the LinkedList is also O(n)  and the same applied to the blockchain implementation.
- The worst case time for search from the LinkedList is also O(n)  and the same applied to the blockchain implementation.

###Space complexity
- The space complexity for storing a LinkedList is O(n) where n is the number of nodes

---