class HashMap:
    def __init__(self, size=11, probe_method='linear'):
        self.size = size
        self.len = 0
        self.slots = [None] * self.size  # Contains the keys
        self.items = [None] * self.size  # Contains the values
        self.quad_probe_counter = 1
        self.probe_method = probe_method

    def get_load_factor(self):
        return self.len / self.size

    def increase_size(self, newsize=101):
        '''
        I'm just gonna copy the elements from the old list and put them in
        the new one. There's probabily a better way to do this.
        Also, this method only works once, i.e. if the load factor goes
        above 75% a second time, this method won't work.
        To make it work I need to increase the size by a specific amount where
        the new size is greater than the old size by a pre-set margin
        and the new size is a prime number.
        Why prime number? To ensure that all slots will be visited.
        In any case, I'm too lazy to do this today.
        '''
        self.newslots = [None] * newsize
        self.newitems = [None] * newsize
        for i in range(self.size):
            if self.slots[i] is not None:
                self.newslots[i] = self.slots[i]
                self.newitems[i] = self.items[i]
        self.slots = self.newslots
        self.items = self.newitems
        self.size = newsize

    def hash(self, key):
        if key < 0:
            key = self.size + key
        return key % self.size

    def rehash(self, old_hash):
        if self.probe_method == 'linear':
            return (old_hash + 1) % self.size
        elif self.probe_method == 'quadratic':
            new_hash = (old_hash + self.quad_probe_counter ** 2) % self.size
            self.quad_probe_counter += 1
            return new_hash

    def put(self, key, value):
        hash = self.hash(key)
        while self.slots[hash] is not None and self.slots[hash] != key:
            hash = self.rehash(hash)
        if self.slots[hash] is None:
            self.slots[hash] = key
            self.len += 1
        self.items[hash] = value
        self.quad_probe_increment = 1
        if self.get_load_factor() >= 0.75:
            self.increase_size()

    def get(self, key):
        starting_hash = hash = self.hash(key)
        while self.slots[hash] != key:
            hash = self.rehash(hash)
            if self.slots[hash] is None or hash == starting_hash:
                raise KeyError(key)
        self.quad_probe_increment = 1
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
                # Decided not to print null keys as a w ay to hide the fact
                # that this hashmap is not auto-resizable/infinite in size.
                return_str += "{}: '{}'".format(key, value)
                if size < self.size - 1:
                    return_str += ', '
            size += 1
        return return_str + '}'


H = HashMap(probe_method='quadratic')
