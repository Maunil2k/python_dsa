# check whether a string is palindrome or not
import sys
sys.setrecursionlimit(1000)

def method1(string: str)-> bool:
    '''
    This approach takes the original string and another reversed one and compares them
    '''
    str1 = string
    str2 = string[::-1]
    for idx in range(len(str1)):
        if str1[idx] == str2[idx]:
            continue
        else:
            return False
    return True

def method2(string: str, start: int, end: int)-> bool:
    '''
    this approach implements recursion
    '''
    if start>=end: #base condition 1
        return True
    elif string[start] != string[end]: #base condition 2
        return False
    else:
        return method2(string, start+1, end-1)

if __name__ == "__main__":
    s = input("Enter a string: ")
    print(method2(s, 0, len(s)-1))