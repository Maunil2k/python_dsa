def insertion_sort(nums: list)-> list:
    if len(nums)<=1:
        return nums
    for start in range(len(nums)):
        pos = start
        while pos>0 and nums[pos] < nums[pos-1]:
            nums[pos], nums[pos-1] = nums[pos-1], nums[pos]
            pos -=1
    return nums

if __name__ == '__main__':
    nums = []
    for idx in range(int(input("Enter number of elements: "))):
        nums.append(int(input(f"Enter at index {idx}: ")))
    print("Original array: {}".format(nums))
    nums = insertion_sort(nums)
    print("Sorted array: {}".format(nums))