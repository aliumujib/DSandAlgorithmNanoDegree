#Dutch National Flag Problem

I didn't solve this as very quickly, I knew that the solution would be fairly easy if I did the following:
- Move zeroes to the front of the list
- Leave ones in place
- Move twos to the back

However I couldn't quite figure out how to do the swaps in place. One approach would be to loop through the list and copy
each item to the correct position in a new list but that would not have obeyed the constraints for traversal and the space complexity would 
have been O(n). After a quick google search, I discovered that it was similar to the binary search approach but I had to manage indices in a
different way.

###Time complexity
- The time complexity for the final solution is O(n) because the solution would still go through the whole array.

###Space complexity
- The worse case space complexity is O(1) because the sorting is done in place.
---