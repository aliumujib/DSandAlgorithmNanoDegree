#Find Files

This felt rather straight forward, the instructions were clear, I used methods from the os.path package to first ensure the the following:

- the path was to a directory not a file so it could be traversed.
- that it was a valid path that existed in the file system. 

I used assertions to ensure that both conditions were met and then proceeded to recursively go through the paths. I chose recursion here because
it seemed like it'd be easier to write and I really wanted to practise writing recursive code.


###Time complexity
- The time complexity for finding a file is o(n) in the worst case where n is the number of subdirectories the path has.

###Space complexity
- The space complexity is also linear O(m) where m is the depth of the file hierachy as more space would be need to store the methods call frames depending on how deeply nested
the file system being traversed is.

---