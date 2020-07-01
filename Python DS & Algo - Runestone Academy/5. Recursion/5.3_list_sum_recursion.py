def listSum(num_list):
    if len(num_list) is 1:
        return num_list[0]
    return num_list[0] + listSum(num_list[1:])


print(listSum([i for i in range(1, 10)]))
