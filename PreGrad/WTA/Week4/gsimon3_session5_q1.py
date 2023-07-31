def cutRod(price, n):
    val = [0 for x in range(n+1)]
    val[0] = 0
 
    for i in range(1, n+1):
        max_val = -3434545767
        for j in range(i):
             max_val = max(max_val, price[j] + val[i-j-1])
        val[i] = max_val
 
    return val[n]
 
# test cases
arr = [1, 5, 8, 9, 13, 4, 17, 20]
size = 4
print("Max value is: %d"%cutRod(arr, size))

arr = [11, 12,14,23230320,23,44,68,3]
size = 8
print("Max value is: %d"%cutRod(arr, size))