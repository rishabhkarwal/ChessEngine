class Cache:
    def __init__(self):
        self.cache = {}

    def get(self, key):
        #print(self.cache)
        return self.cache.get(key)

    def set(self, key, value):
        self.cache[key] = value

    def remove(self, key):
        if key in self.cache: del self.cache[key]

def cache_function(func):
    cache = Cache()

    def wrapper(*args):
        
        board = tuple(args[0].board)
        cached_result = cache.get(board)
        if cached_result is not None:
            return cached_result

        result = func(*args) # Call the original function and cache the result
        cache.set(board, result)

        return result
    
    wrapper.cache = cache
    return wrapper
