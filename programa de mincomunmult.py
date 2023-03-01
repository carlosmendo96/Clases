def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if (x1 > x2 and v1 >= v2) or (x1 < x2 and v1 <= v2):
        return 'NO'
    if abs(x1-x2)%abs(v2-v1) == 0: 
        return 'YES'
    else:
        return 'NO'
