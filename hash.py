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
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Update value if key already exists
                return
        self.table[index].append([key, value])  # Append the new key-value pair

    def get(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Key not found

    def delete(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return


# Example usage
hash_table = HashTable(size=5)

# Insert key-value pairs
hash_table.insert("Alice", "123-456-7890")
hash_table.insert("Bob", "987-654-3210")
hash_table.insert("Charlie", "555-555-5555")
hash_table.insert("Diana", "444-444-4444")
