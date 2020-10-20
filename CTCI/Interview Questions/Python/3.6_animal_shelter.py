# An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select which specific animal they would like. Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in LinkedList data structure.
# Page 67

# I'm just going to use a Python list instead of a LinkedList.
# Dequeue is going to be O(n) in that case.

class Shelter:
    def _init__(self):
        self.cats = []
        self.dogs = []
        self.counter = 0 # To keep track of order

    def enqueue(self, animal):
        if animal == "dog":
            self.dogs.enqueue(counter)
            counter += 1
        elif animal == "cat":
            self.cats.enqueue(counter)
            counter += 1
        else:
            print("Invalid animal")
            return

    def dequeueAny(self):
        if len(self.cats) == 0:
            if len(self.dogs) == 0:
                return None
            else:
                return self.dogs[0]
        else:
            if len(self.dogs) == 0:
                return self.cats[0]
            else:
                continue
        if self.cats[0] < self.dogs[0]:
            return self.cats.pop(0)
        return self.dogs.pop(0)

    def dequeueDog(self):
        if len(self.dogs) == 0:
            return None
        return self.dogs.pop(0)

    def dequeueCat(self):
        if len(self.cats) == 0:
            return None
        return self.cats.pop(0)
