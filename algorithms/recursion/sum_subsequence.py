# Find all the subsequences whose sum adds upto k
import sys
from array import array as arr
sys.setrecursionlimit(10000)

def sum_subsequences(array: arr, add: int, idx: int=0, temp=[]):
    '''
    prints all the combinations of digits that sum upto add (without repetition)
    '''
    if idx == len(array):
        if sum(temp) == add:
            print(temp)
        return
    temp.append(array[idx])
    sum_subsequences(array, add, idx+1, temp)
    temp.pop()
    sum_subsequences(array, add, idx+1, temp)

def sum_subsequences_with_repetition(array: arr, add: int, idx: int=0, temp=[]):
    pass

if __name__ == '__main__':
    array = arr('i', [1,2,3,4,5,6])
    sum_subsequences(array, 6)
    print('qer'*3)