def unique_paths(m: int, n: int, ans=0):
    if m == 1 or n == 1:
        return 1
    else:
        return unique_paths(m, n-1) + unique_paths(m-1, n)

if __name__ == '__main__':
    #print(ans)
    print(unique_paths(3,3))
    #print(ans)