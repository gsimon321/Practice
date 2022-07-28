def firecracker(MO):
    columns = set()
    rows = set()

    for i in range(len(MO)):
        for j in range(len(MO[i])):
            if MO[i][j] == 0:
                columns.add(i)
                rows.add(j)
            
    
    for i in range(len(MO)):
        for j in range(len(MO[i])):
            if columns.__contains__(i) or rows.__contains__(j):
                MO[i][j] = 0
    
    return MO

# test cases
test1 = [
    [5, 0, 0, 5, 8],
    [9, 8, 10, 3, 9],
    [0, 0, 2, 3, 1],
    [8, 0, 6, 7, 2],
    [0, 1, 8, 123, 1]
]

test2 = [
    [5, 2, 8, 5, 8],
    [9, 8, 11, 0, 99],
    [11, 7, 2, 3, 1],
    [8, 10, 6, 7, 2],
    [4, 1, 0, 5, 10]
]

print(firecracker(test1))
print(firecracker(test2))



