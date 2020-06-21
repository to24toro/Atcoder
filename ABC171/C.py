N = int(input())
def change(x):
    if x==0: x=26
    return chr(ord('a')+int(x)-1)
def helper(N,x):
    if N<=26: return change(N)
    if (int(N/x)):
        if N%x !=0:
            return helper(int(N/x),x)+change(N%x)
        else:
            return helper(int(N/x)-1,x)+change(N%x)
print(helper(N,26))