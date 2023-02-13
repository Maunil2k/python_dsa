def selection_sort(nums: list)-> list:
    '''
    In selection sort, we execute the following steps:
    1) start position = 0, look for the smallest number in the remaining list
    2) once that value is found(say ith position) , swap start and ith value
    3) increment the start value by 1
    4) Repeat steps 1-3 until end of list is reached
    '''
    for start in range(len(nums)):
        min_pos = start
        for idx in range(start, len(nums)):
            if nums[idx] < nums[min_pos]:
                min_pos = idx
        nums[start], nums[min_pos] = nums[min_pos], nums[start]

    return nums

if __name__ == '__main__':
    nums = []
    for idx in range(int(input("Enter number of elements: "))):
        nums.append(int(input(f"Enter at index {idx}: ")))
    print("Original array: {}".format(nums))
    nums = selection_sort(nums)
    print("Sorted array: {}".format(nums))