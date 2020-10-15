dic = {'A':'a','B':'b','C':'c'}
n,k = map(int,input().split())
k -=1
S = input()
print(S[:k] + dic[S[k]]+S[k+1:])