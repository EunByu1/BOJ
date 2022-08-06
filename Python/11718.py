while(1) :
    try :
        print(input())     
    # 입력값이 안들어온다면(EOF, End Of File)
    except EOFError:
        break
