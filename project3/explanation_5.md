#Autocomplete with Tries

I found this very interesting, maybe because it was more practical and I had seen the auto complete feature at work before, I had to do a bit of revision on how to setup and traverse a Trie,
and after some thing I was able to recursively traverse all the nodes of the trie and added all the complete words to a list. 

###Time complexity
- The time complexity for the final solution is O(n) because the solution would still go through the whole Trie.

###Space complexity
- The worse case space complexity is O(n) because the size of the array depends on the number of child nodes the 
prefix node has.
---