# Print all positive integers to the equation a^3 + b^3 = c^3 + d^3 where a, b, c, d are integers between 1 and 100

# Naive Solution - O(n^4)
def find_pairs_naive():
    for a in range(1, 1001):
        for b in range(1, 1001):
            for c in range(1, 1001):
                for d in range(1, 1001):
                    if a ** 3 + b ** 3 == c ** 3 + d ** 3:
                        print('[{}, {}, {}, {}]'.format(a, b, c, d))
                        break

# Suboptimal Solution - O(n^2)
def find_pairs_suboptimal():
    hashmap = {}
    for a in range(1, 1001):
        for b in range(1, 1001):
            result = a ** 3 + b ** 3
            if result not in hashmap:
                hashmap[result] = []
            hashmap[result].append([a, b])

    for c in range(1, 1001):
        for d in range(1, 1001):
            result = c ** 3 + d ** 3
            if result in hashmap:
                for lst in hashmap[result]:
                    print(lst, c, d)

# Optimal Solution - O(n^2)
def find_pairs_optimal():
    hashmap = {}
    for a in range(1, 1001):
        for b in range(1, 1001):
            result = a ** 3 + b ** 3
            if result not in hashmap:
                hashmap[result] = []
            hashmap[result].append([a, b])

    for result in hashmap:
        for lst in hashmap[result]:
            print(lst, lst)



# find_pairs_naive()
find_pairs_suboptimal()
find_pairs_optimal()
