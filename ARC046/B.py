N = int(input())
A, B = map(int,input().split())
if N <= A:
    print("Takahashi");exit()
if N <= B + 1:
    print("Aoki");exit()
if A == B:
    if N % (A + 1) != 0:
        print("Takahashi")
    else:
        print("Aoki")
else:
    if A > B:
        print("Takahashi")
    else:
        print("Aoki")