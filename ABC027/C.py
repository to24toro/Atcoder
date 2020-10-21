n = int(input())
N = bin(n)
l = len(N)-2
j = 1
for i in range(l):
    if l%2==0:
        if i%2==1:
            j = 2*j+1
        else:
            j *=2
    else:
        if i%2==0:
            j = 2*j+1
        else:
            j *=2

    if j>n:
        if i%2==0:
            print('Aoki')
        else:
            print('Takahashi')
        exit()