 n = len(arr)
    print("{:1.6f}".format(len([a for a in arr if a>0])/n))
    print("{:1.6f}".format(len([a for a in arr if a<0])/n))
    print("{:1.6f}".format(len([a for a in arr if a==0])/n))
    
