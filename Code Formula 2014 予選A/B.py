a,b = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
A = ['x']*10
for i in p:
    A[i]='.'
for i in q:
    A[i]='o'

print(A[7]+' '+A[8]+' '+A[9]+' '+A[0])
print(' '+A[4]+' '+A[5]+' '+A[6] + ' ')
print(' '+' '+A[2]+' '+A[3]+' '+' ')
print(' '+'  '+A[1]+'  '+' ')