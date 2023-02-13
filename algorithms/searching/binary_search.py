# finding target index in a list sorted in increasing order
from time import time

def find_first_occurrence(nums: list, position: int):
    if position == 0:
        return position
    else:
        if nums[position-1] == nums[position]:
            position = position - 1
            return find_first_occurrence(nums, position)
        elif nums[position-1] != nums[position]:
            return position

def binary_search(nums: list, target: int):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        #print("Hi: ", hi, 'Lo:', lo, "mid: ", mid)
        if target == nums[mid]:
            return find_first_occurrence(nums, mid)
        elif mid > 0 and target <= nums[mid-1]:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

def linear_search(elements: list, query: int):
    for idx, val in enumerate(elements):
        if val == query:
            return idx
    return -1

if __name__ == '__main__':
    nums = [i for i in range(10000000)]
    # print("Enter size of the list first and values in increasing order")
    # for i in range(int(input("list size: "))):
    #     nums.append(int(input(f"input at index {i}: ")))
    target = int(input("Target integer: "))
    t1 = time()
    print("Target index: ", linear_search(nums, target))
    t2 = time()
    print("Target index: ", binary_search(nums, target))
    t3 = time()
    print(f'Time taken by linear search: {(t2-t1)}s')
    print(f'Time taken by binary search: {(t3-t2)}s')