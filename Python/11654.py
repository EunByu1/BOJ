Input = input()

try:
    print(ord(Input))
    
except TypeError:
    print(chr(int(Input)))
