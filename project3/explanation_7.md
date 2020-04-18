#Autocomplete with Tries

This was very similar to problem 5, I applied the same logic of traversing a trie. The trailing slash handler seemed 
like it could be handled by filtering out its effects early enough, so that's what I did. 
I'd like to know if there's a better approach

###Time complexity
- The time complexity for the final solution is O(n) because the solution would still go through the whole Trie.

###Space complexity
- The worse case space complexity for the find operation is O(n) because the size of the split array depends on the number 
of sub-paths in the path e.g /home/about/me will produce array [home,about,me].
---