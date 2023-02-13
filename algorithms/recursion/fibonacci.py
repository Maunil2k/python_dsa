import sys
sys.setrecursionlimit(1000)

#fib series: 0, 1, 1, 2, 3, 5, 8, 13, 21
#index:      0, 1, 2, 3, 4, 5, 6,  7,  8

def fibonacci(n: int)-> int:
    assert n>=0, "n must be greater than or equal to zero"
    if n==0: #base case 1
        return 0
    elif n ==1 or n==2: #base case 2
        return 1
    else:
        val1 = fibonacci(n-1) #recursion call 1
        val2 = fibonacci(n-2) #recursion call 2
        return val1 + val2 #small calculation

if __name__ == "__main__":
    print(fibonacci(int(input("Enter a number: "))))