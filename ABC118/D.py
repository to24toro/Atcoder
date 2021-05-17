n,m = map(int,input().split())
A = list(map(int,input().split()))
dic = {1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
def helper(n,A):
    if n==0:
        return 0
    elif n<0:
        return -float('inf')
    ans = []
    for a in A:
        ans.append(helper(n-dic[a],A)*10+a)
    return max(ans)
print(helper(n,A))