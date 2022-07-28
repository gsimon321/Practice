def subTemp(degrees) -> bool:
        subList = set()
        counter = 0
        for i in range(len(degrees)):
            counter = counter + degrees[i]

            if  counter in subList or counter == 0:
                return True

            subList.add(counter)
        return False
        
    

# Tests
arr = [-3, 2, 3, 1, 6]
print("this is the first test:", subTemp(arr))

arr = [4, 2, -3, 1, 6]
print("this is the second test:", subTemp(arr))






