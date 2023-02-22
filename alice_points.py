alice_points = 0
    bob_points = 0
    l = []
    for i in range(3):
        if a[i] > b[i]:
            alice_points += 1
        elif a[i] < b[i]:
            bob_points += 1
    else:
        pass
    return(alice_points, bob_points)