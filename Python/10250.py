t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    num = n//h + 1
    floor = n % h
    
    # h의 배수이면,
    if n % h == 0:  
        num = n//h
        floor = h
        
    print(f'{floor*100+num}')
