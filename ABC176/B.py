N = input()
cnt = 0
for n in N:
    cnt +=int(n)
print('Yes' if cnt%9==0 else 'No')