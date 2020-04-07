#LRU Cache

I found this problem quite interesting, to implement the least recently used functionality I used a deque() from the python collections library 
to store the keys as they are being inserted and remove from the head of the queue when it full, I then check for correct sizes of the map and the queue.
Using a hashmap seemed like the logical thing to do for a Key-Value pair kind of data store so I went with it, also for the obvious constant insertion and retrieval advantages.

###Time complexity
- The time complexity for insertion into the cache is o(1) as all the operations involved run in constant time.
- The time complexity for retrieval from the cache is also o(1) as all the operations involved run in constant time.

###Space complexity
- The space complexity for insertion into the cache is constant because the cachesize never doubles but instead discards 
unused elements.

---