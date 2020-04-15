#Max and Min in a Unsorted Array

Initially, I solved this by going through the array and changing the max and min value as necessary, you will find the
function that uses this approach in __get_min_max_recursive__(). I think it satisfied the constraints and is fairly simple.
I was doing some extra study on divide and conquer algorithms and coincidentally found an example that solved the problem using
divide and conquer, I was able to listen to just the algorithm and wrote the code myself. You will find that solution in
__get_min_max_div_and_conquer__().

###Time complexity
- The time complexity for the final get_min_max_recursive is O(n) because the solution would still go through the whole array.
- The time complexity for the final get_min_max_div_and_conquer is O(n log (n)) because the number of comparisons reduces
each time the function is recursively called.

###Space complexity
- The worse case space complexity is O(1) for get_min_max_recursive because no new array is created except for returning the results and that's negligible.
- The worse case space complexity is O(n) for get_min_max_div_and_conquer because new arrays are created to perform the comparisons.
---