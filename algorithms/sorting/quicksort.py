def quicksort(nums: list, left: int, right: int):
    '''
    :param nums: list of integers
    :param left: left index
    :param right: right index
    :return: sorted list
    '''
    if left<right:
        partition_pos = partition(nums, left, right)
        quicksort(nums, left, partition_pos-1)
        quicksort(nums, partition_pos+1, right)

def partition(nums, left, right):
    #right points at the pivot element
    i = left
    j = right - 1
    pivot_element = nums[right]
    while i <= j:
        if nums[i]<pivot_element:
            i+=1
        elif nums[j]>pivot_element:
            j-=1
        else:
            nums[i], nums[j] = nums[j], nums[i]
    if nums[i]>pivot_element:
        nums[i], nums[right] = nums[right], nums[i]
    #return i which will be used further to split the array
    return i

if __name__ == '__main__':
    nums = []
    for i in range(int(input("Input array size: "))):
        nums.append(int(input(f"Element at index {i}: ")))
    print("Original array: ", nums)
    quicksort(nums=nums, left=0, right=len(nums)-1)
    print("Sorted array  : ", nums)