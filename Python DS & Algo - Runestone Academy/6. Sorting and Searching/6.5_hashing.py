class HashMap:
    def __init__(self, size=11):
        self.size = size
        self.len = 0
        self.slots = [None] * self.size  # Contains the keys
        self.items = [None] * self.size  # Contains the values

    def hash(self, key):
        if key < 0:
            key = self.size + key
        return key % self.size

    def rehash(self, old_hash, skip=1):
        return (old_hash + skip) % self.size

    def put(self, key, value):
        hash = self.hash(key)
        while self.slots[hash] is not None and self.slots[hash] != key:
            hash = self.rehash(hash)
        if self.slots[hash] is None:
            self.slots[hash] = key
            self.len += 1
        self.items[hash] = value

    def get(self, key):
        starting_hash = hash = self.hash(key)
        while self.slots[hash] != key:
            hash = self.rehash(hash)
            if self.slots[hash] is None or hash == starting_hash:
                return None
        return self.items[hash]

    def __delitem__(self, key):
        hash = first_hash = self.hash(key)
        while self.slots[hash] is not None:
            if self.slots[hash] == key:
                self.slots[hash] = None
                self.items[hash] = None
                self.len -= 1
            hash = self.rehash(hash)
            if hash == first_hash:
                raise KeyError(key)
        raise KeyError(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __len__(self):
        return self.len

    def __contains__(self, key):
        return key in self.slots
        # This is kinda cheaty but this is Python I guess lol
        # Too lazy for a for loop
        # But not too lazy for commenting something longer
        # Hmmm...

    def __str__(self):
        # Function assumes that keys are integers are their values are strings.
        return_str = '{'
        size = 0
        for key, value in zip(self.slots, self.items):
            if key is not None:
                # Decided not to print null keys as a way to hide the fact
                # that this hashmap is not auto-resizable/infinite in size.
                return_str += "{}: '{}'".format(key, value)
                if size < self.size - 1:
                    return_str += ', '
            size += 1
        return return_str + '}'


H = HashMap()
H[-1] = "cattus maximus"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"
H[20] = 'duck'
print(H)
print(len(H))
del H[202]
print(H)
print(len(H))
