#Square root of a number (floored)

I spent the two days of working on this project trying to implement the approach described at https://www.freecodecamp.org/news/find-square-root-of-number-calculate-by-hand/ for 
finding the square root of a number by hand, well that was a waste of time 🙂. Later was able to correctly find the square root of any number by running a loop from 0 to the target(t) which checked for
any number (n) where 0 <= n <= t, if if n*n > t, return n - 1. This was a simple mechanical solution that worked for the most part. I tried to optimize it myself to meet the time complexity constraints
but got stuck. After a quick google search, I was able to improve the solution by approaching it like binary search.


###Time complexity
- The time complexity for the final solution is O(log(n)) since the search space is halved every time.

###Space complexity
- The worse case space complexity is O(log(n)).
---