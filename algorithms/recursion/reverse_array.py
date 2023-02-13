# Q: return a reversed list / array
import sys
sys.setrecursionlimit(1000)

def reverse_array(array: list, start: int, end: int)-> list:
    '''
    This approach uses recursion
    '''
    if start>=end:
        return array
    else:
        array[start], array[end] = array[end], array[start]
        return reverse_array(array, start+1, end-1)

if __name__ == '__main__':
    nums = []
    for i in range(int(input("Enter the size of array: "))):
        nums.append(int(input(f"Enter value at index {i}: ")))
    print(f"Your array: {nums}")
    print(f"Reversed array: {reverse_array(nums, 0, len(nums)-1)}")