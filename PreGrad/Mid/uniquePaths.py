def uniquePath(m: int, n: int, memo = None) -> int:
    key = str(m) + ',' + str(n)
    if memo == None:
       memo = {}
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n ==0:
        return 0
        
    memo[key] =  uniquePath(m - 1, n, memo) +  uniquePath(m, n - 1, memo)
    return memo[key]

print(uniquePath(18,18))