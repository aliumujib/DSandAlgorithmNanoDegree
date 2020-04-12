#Find Files

This felt rather straight forward, the instructions were clear, I used methods from the os.path package to first ensure the the following:

- the path was to a directory not a file so it could be traversed.
- that it was a valid path that existed in the file system. 

I used assertions to ensure that both conditions were met and then proceeded to recursively go through the paths. I chose recursion here because
it seemed like it'd be easier to write and I really wanted to practise writing recursive code.


###Time complexity
- the time complexity would be O(n^2) in the worst case where n is the depth of the group hierarchy. I arrived at this idea by thinking of the folder structure
as a non binary tree and the traversal algorithm as a BFS traversal of the tree which as complexity of O(n) + O(n-1) + O(n-2) + .. + O(1) which is O(n^2)..

###Space complexity
- The space complexity is also linear O(m) where m is the depth of the file hierarchy as more space would be need to store the methods call frames depending on how deeply nested
the file system being traversed is.

---