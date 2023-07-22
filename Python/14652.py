N, M, K = map(int, input().split())

count = 0
value = 0

while(1):
    count = count + 1
    
    if(M * count > K):
        value = K - (M * (count - 1))
        print(count-1, value)
        break
