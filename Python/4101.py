while(1):
    n, m = map(int, input().split())

    if(n > m):
        print("Yes")
    elif(n == 0 and m == 0):
        break
    elif(n < m) or (n == m):
        print("No")
