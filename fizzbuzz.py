def fizzBuzz(n):
    # Write your code here

    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        if i % 3 != 0 and i % 5 == 0:
            print("Buzz")
        if i % 3 != 0 and i % 5 != 0:
            print(i)   
if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
