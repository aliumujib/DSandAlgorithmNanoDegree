#User group

I found this also very straight forward, to solve it I recursively traversed the lists of lists and compared the userIds for each user 
until I found or didn't find the user I was searching for, if I found the user, then the result true is returned, else I return false.

###Time complexity
- The time complexity for the search can be calculated as follows:
When the function finds the group name at the first level, i.e group name is equal to the group passed the first time, the time complexity is O(1)
Otherwise the time complexity could be O(n^2) where n is the depth of the group hierarchy. I arrived at this idea by thinking of the user group structure
as a tree and the traversal algorithm as a BFS traversal of the tree which as complexity of O(n) + O(n-1) + O(n-2) + .. + O(1) which is O(n^2).

###Space complexity
- The space complexity for this operation is O(m) in the worst case where m is the depth of the subgroups.
---