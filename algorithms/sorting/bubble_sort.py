#Sorting the list in increasing order

def bubble_sort(nums: list)-> list:
    for _ in range(len(nums)-1):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums

if __name__ == '__main__':
    nums = []
    for i in range(int(input("Size of the list: "))):
        nums.append(int(input(f"Element at index {i}: ")))
    print("Sorted list: ", bubble_sort(nums))