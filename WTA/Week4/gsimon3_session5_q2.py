from sys import maxsize

def maxSubArraySum(a):
    size = len(a)
    max = -maxsize - 1
    maxEnd = 0
    st = 0
    e = 0
    s= 0
    count = 0;
    
    for i in range (0,size):

        maxEnd += a[i]
        if max < maxEnd:
            max = maxEnd
            st = s
            e = i
        if maxEnd < 0:
            maxEnd = 0
            s = i+1
    
    diff = e - st + 1
    print(diff);

# test cases
a = [-2, -3, 63]
maxSubArraySum(a)
a = [1, -2, 22, 1, -24, 1]
maxSubArraySum(a)
