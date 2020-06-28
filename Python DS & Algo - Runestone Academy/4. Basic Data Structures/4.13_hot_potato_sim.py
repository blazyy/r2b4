from queue import Queue

def hot_potato(people, num_passes):
    queue = Queue()
    for person in people:
        queue.enqueue(person)

    while queue.size() != 1:
        for i in range(num_passes):
            queue.enqueue(queue.dequeue())
        queue.dequeue()

    return queue.dequeue()

names = ['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad']
print(hot_potato(names, 7)) # Susan
