"""
Problem: You are given as input a list of data requests of length (N) and a cache of size (K). When you are processing
         a particular data request, if it is not already in your cache then this is a called a cache miss. When this
         happens you have to evict an item from the cache & place your current item in the cache. The goal is to make
         a sequence of eviction decisions that lead to the least amount of cache misses over the entire array of
         data requests.

Claim: A furthest-in-future eviction strategy leads to an optimal caching algorithm.

Proof: Too tricky for me.

"""


class CacheManager:
    def __init__(self, data_requests, cache_size):
        self.data_requests = data_requests
        self.num_requests = len(data_requests)
        self.cache_size = cache_size
        self.cache = {}
        self.idx_lookup = {}

    def init_cache(self):
        num_in_cache = 0
        for req in self.data_requests:
            if self.cache.get(req, None) is None:
                if num_in_cache < 2:
                    self.cache[req] = True
                    num_in_cache += 1
                else:
                    break

    def init_idx_lookup(self):
        for i in range(self.num_requests - 1, -1, -1):
            req = self.data_requests[i]
            if self.idx_lookup.get(req, None) is None:
                self.idx_lookup[req] = [i]
            else:
                self.idx_lookup[req].append(i)

    def find_furthest_in_future(self):
        furthest_in_future = [None, -1]
        for item in self.cache.keys():
            if self.idx_lookup[item][-1] > furthest_in_future[1]:
                furthest_in_future = [item, self.idx_lookup[item][-1]]

        return furthest_in_future

    def process_requests(self):
        num_in_cache = len(self.cache)

        evictions = []
        for req in self.data_requests:
            self.idx_lookup[req].pop()
            if num_in_cache < self.cache_size:
                self.cache[req] = True

            if self.cache.get(req, None) is None:  # not in cache
                # make eviction decision
                furthest_in_future = self.find_furthest_in_future()
                del self.cache[furthest_in_future[0]]
                self.cache[req] = True
                evictions.append(furthest_in_future[0])
            else:
                evictions.append(None)

            # If this item does not appear any more in the list then we need to delete it from the cache.
            # This is because furthest_in_future() will fail when looking up its last index, that DNE.
            if len(self.idx_lookup[req]) == 0:
                del self.cache[req]
                num_in_cache -= 1

        return evictions

    def compute(self):
        # 1. Initialize cache to be first (cache_size) distinct items
        self.init_cache()

        # 2. Initialize direct address table w/ chaining to map item --> indices in Request array
        self.init_idx_lookup()

        # 3. Process requests, keeping track of eviction decisions
        evictions = self.process_requests()

        return evictions


if __name__ == '__main__':
    data_requests = ['a', 'b', 'c', 'b', 'c', 'b', 'a', 'a']
    cache_size = 2

    cache_manager = CacheManager(data_requests=data_requests,
                                 cache_size=cache_size)

    evictions = cache_manager.compute()
    
    print(evictions)
