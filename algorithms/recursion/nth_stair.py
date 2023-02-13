# problem link: https://practice.geeksforgeeks.org/problems/count-ways-to-reach-the-nth-stair-1587115620/1?utm_source=inf&utm_medium=inf%2Fcampaign+&utm_campaign=codein10_nthstair_YT
'''
There are n stairs, a person standing at the bottom wants to reach the top.
The person can climb either 1 stair or 2 stairs at a time.
Count the number of ways, the person can reach the top (order does matter).
'''

import sys
sys.setrecursionlimit(1000)

def count_ways(num_stairs: int)-> int:
    assert num_stairs>0, "num of stairs must be greater than zero"
    if num_stairs == 1: #base case 1
        return 1
    elif num_stairs == 2: #base case 2
        return 2
    else:
        val1 = count_ways(num_stairs-1) #recursion call 1
        val2 = count_ways(num_stairs-2) #recursion call 2
        return val1 + val2 #small calculation

if __name__ == '__main__':
    print(count_ways(int(input("Enter a number: "))))