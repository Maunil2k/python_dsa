import sys
sys.setrecursionlimit(1000)
# question link: https://practice.geeksforgeeks.org/problems/power-set4302/1?utm_source=inf&utm_medium=inf%2Fcampaign+&utm_campaign=codein10_powerset_YT
def subsequences(array: list, i=0, temp=[]):
    global answer
    if i == len(array):
        print(temp)
        return
    temp.append(array[i])
    subsequences(array, i+1, temp)
    temp.pop(-1)
    subsequences(array, i+1, temp)


subsequences([1,2,3])