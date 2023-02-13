from array import array as arr
'''
Docs: https://docs.python.org/3/library/array.html
Data types in arrays:
1) 'b' -> signed char
2) 'B' -> unsigned char
3) 'h' -> signed short int
4) 'H' -> unsigned short int
5) 'i' -> signed integer
6) 'I' -> unsigned int
7) 'l' -> signed long int
8) 'L' -> unsigned long int
9) 'q' -> signed long long int
10) 'Q' -> unsigned long long int
11) 'f' -> float
13) 'd' -> double
'''
if __name__ == '__main__':
    nums = []
    for idx in range(int(input("Enter size of the array: "))):
        nums.append(int(input("Enter element at index {}: ".format(idx))))
    nums = arr('i', nums)

    #inserting an element at a given index, Time complexity: O(N)
    nums.insert(3,0) #index, value
    print(nums)

    #appending to an array, Time complexity: O(1)
    nums.append(5) #appends the element to the array