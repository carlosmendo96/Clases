def getTotalX(a, b):
    # Write your code here
    count = 0
    for i in range(min(a), max(b)+1):
        if all([i%x == 0 for x in a]) and all([x%i==0 for x in b]):
            count += 1
    return count  
