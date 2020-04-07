#Union and Intersection

This seemed like the kind of operation to use a set for because it could automatically help with deduplication. 
- For the Union operation I looped through both lists and appended their contents to the set, that automatically gave the unique contents of both LinkedLists, I then used another another loop
to convert the set into another LinkedList.
- For the Intersection, I used added the contents of both LinkedLists to separate sets, and used the set intersection operator to find the intersection,
alternatively I could have looped found the union and then gone through each element in the union to check if it was contained in both sets but I felt
it'd be less efficient than the existing implementation for the set class.

###Time complexity
- The worst case time complexity for Union is O(n) because there are a number of loops but none is nested.
- The worst case time complexity for intersection is O(n) + O(k) where k is the minimum len of either LinkedList.

###Space complexity
- The space complexity for both operations is O(n)

---