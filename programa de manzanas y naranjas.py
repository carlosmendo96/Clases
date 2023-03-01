def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apple_c = 0
    orange_c = 0

    for apple in apples:
        if s <= a+apple <= t:
            apple_c += 1
    for orange in oranges:
        if s <= b+orange <= t:
            orange_c += 1
    print(apple_c)
    print(orange_c)

