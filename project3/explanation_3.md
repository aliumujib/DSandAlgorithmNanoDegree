#Rearrange Array Elements

I was able to solve this on my own. after a bit of thought, I figured that the largest sum would come as a result of having the largest digits 
on the list as the first digits of the sum pair and the second largest digits as the second digits of the numbers in the pair sum etc. the second hint for me was in the time complexity limit and the word rearrange. I knew I had to find
a sorting algorithm that could sort under those constraints so I chose merge sort. After sorting, I looped through the list and used the index of each number
to add it to a string. Then I converted the string to int and returned the pair in a list. 

###Time complexity
- The time complexity for the final solution is O(n log(n)) because the time complexity for merge sort  O(n log(n)) and the time complexity for the 
second loop can be largely ignored i.e O(n log(n)) + O(n) = O(n log(n)).

###Space complexity
- The worse case space complexity is O(n) because the amount of space needed will grow with the data since the sorting isn't done in place.
---