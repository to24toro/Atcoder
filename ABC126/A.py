n,k = map(int,input().split())
S = [s for s in input()]
S[k-1] = S[k-1].lower()
print(''.join(S))