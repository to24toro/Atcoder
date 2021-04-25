n = int(input())
for i in range(1,n+1):
    if i*(i+1)//2>=n:
        s = i*(i+1)//2-n
        idx = i
        break
for i in range(1,idx+1):
    if s!=i:
        print(i)