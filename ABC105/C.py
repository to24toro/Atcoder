n=int(input())

ans = ''
n = -n
while n !=0:
    ans += str(-(n%-2))
    n //=-2
print(ans[::-1] if ans != '' else 0)
