from collections import deque


class LRU_Cache(object):

    def __init__(self, capacity):
        self.recency_tracker = deque()
        self.max_size = capacity
        self.cache = {}

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        else:
            return -1

    def is_full(self):
        return len(self.recency_tracker) >= self.max_size

    def set(self, key, value):
        if(self.is_full()):
            least_recently_used_key = self.recency_tracker.popleft()
            del self.cache[least_recently_used_key]

        assert len(self.recency_tracker) < self.max_size

        self.recency_tracker.append(key)
        self.cache[key] = value


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
res = our_cache.get(9)      # returns -1 because 9 is not present in the cache
print(res)

our_cache.set(5, 5)
our_cache.set(6, 6)

# returns -1 because the cache reached it's capacity and 1 was the least recently used entry
res = our_cache.get(1)
print(res)
