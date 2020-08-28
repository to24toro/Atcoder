n = int(input())

S = input()
T  = ''
for s in S:
    T+=(chr(ord('A')+(ord(s)-ord('A')+n)%26))
print(T)