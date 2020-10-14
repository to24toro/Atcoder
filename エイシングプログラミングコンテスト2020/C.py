N = int(input())
A = [0]*(61206)
def calc(x,y,z):
    return x**2+y**2+z**2+x*y+y*z+z*x
for x in range(1,101):
    for y in range(1,101):
        for z in range(1,101):
            A[calc(x,y,z)] += 1
for i in range(1,N+1):
    print(A[i])