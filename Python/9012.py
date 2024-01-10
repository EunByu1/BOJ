# Stack 활용 문제 
for _ in range(int(input())):
    stk = []
    isVPS = True

    for ch in input():
        if ch == "(":
            stk.append(ch)
        else:
            if stk:
                stk.pop(-1)
            else:
                isVPS = False
                break
    if stk:
        isVPS = False

    print("YES" if isVPS else "NO")
