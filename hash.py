class HashTable:
    def __init__(self, size=10):
        """Initialize the hash table with a fixed size."""
        self.size = size
        self.table = [[] for _ in range(size)]  # Create a list of empty lists for chaining

    def _hash_function(self, key):
        """Hash function to calculate the index for a given key."""
        return hash(key) % self.size
        
    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash_function(key)
