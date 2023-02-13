import sys
sys.setrecursionlimit(1000)

def powers_of_two(n: int)-> int:
    assert n>=0, "n must be greater than or equal to zero"
    if n==0: #base case 1
        return 1
    elif n==1: #base case 2
        return 2
    else:
        val = powers_of_two(n-1) #recursion call
        return 2 * val #small calculation

if __name__ == "__main__":
    print(powers_of_two(int(input("Enter a number: "))))