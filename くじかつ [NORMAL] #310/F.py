n = int(input())
A = list(input())
A = [int(i)-1 for i in A]
B = [0 if i%2==0 else i for i in A]
cnt = 0
for i in range(n):
    if B[i]%2:
        if (n-1)&i==i:
            cnt += 1
if cnt%2:
    print(1)
else:
    if 1 in B:
        print(0)
    else:
        C = [i//2 if i%2==0 else i for i in A]
        cnt = 0
        for i in range(n):
            if C[i]%2:
                if (n-1)&i==i:#mod2のnCrをもとめるほうほう
                    cnt += 1
        if cnt%2:
            print(2)
        else:
            print(0)
