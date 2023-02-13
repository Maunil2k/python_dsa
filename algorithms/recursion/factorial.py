import sys
sys.setrecursionlimit(1000) #upper limit for recursion calls

def factorial(n: int)->int:
    assert n >= 0, "n must be greater than or equal to zero"
    if n<=1: #base case - this is where our recursion calls must stop
        return 1
    else:
        val = factorial(n-1) #recursion call
        return val * n #small calculation

if __name__ == "__main__":
    print(factorial(int(input("Enter a number: "))))