#Search in a Rotated Sorted Array

I got very stuck on this and tried a number of approaches such as generalizing that the pivot item would always be in the middle, needless to say
that didn't work. I later discovered after a quick search on google that the trick was to find the pivot item, but looking at the center of the array
and working back to find which item on the list had a lesser item on the left. After that I could decide to search the left side of the array if the 
target was greater than the pivot value and the right side if it was less than the pivot value. It was a good opportunity to practise my 
binary search.

###Time complexity
- The time complexity for the final solution is O(log(n)) since the search space is halved every time binary search is used.

###Space complexity
- The worse case space complexity is O(log(n)).
---