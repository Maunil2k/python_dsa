from time import time
def merge_algo(nums1: list, nums2: list)->list:
    sorted_list = []
    i, j = 0, 0
    while i<len(nums1) and j<len(nums2):
        if nums1[i]>nums2[j]:
            sorted_list.append(nums2[j])
            j+=1
        else:
            sorted_list.append(nums1[i])
            i+=1
    return sorted_list + nums1[i:] + nums2[j:]

def divide_and_conquer(nums: list)->list:
    if len(nums)<=1:
        return nums
    else:
        mid = len(nums) // 2
        left, right = nums[:mid], nums[mid:]
        left_part, right_part = divide_and_conquer(left), divide_and_conquer(right)
    sorted_list = merge_algo(left_part, right_part)
    return sorted_list

if __name__ == '__main__':
    nums = []
    for i in range(int(input("Number of elements in the list: "))):
        nums.append(int(input(f"Element at index {i}: ")))
    print("Original list: {}".format(nums))
    t1 = time()
    print(f"Sorted List {divide_and_conquer(nums)}")
    print(f"Time taken: {time() - t1}")