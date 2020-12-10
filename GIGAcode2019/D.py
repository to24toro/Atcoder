h,w,k,v = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(h)]
S = [[0]*(w+1)]
ans = 0
for i in range(h):
    tmp = [0]
    for j in range(w):
        tmp.append(tmp[-1]+A[i][j]+S[-1][j+1]-S[i][j])
    S.append(tmp)
for a in range(h):
    for b in range(h,-1,-1):
        if b-a<=0: continue
        for c in range(w+1):
            for d in range(w,-1,-1):
                if d-c<=0: continue
                tmp_v = v-k*(d-c)*(b-a)
                if tmp_v >=0 and tmp_v>= S[b][d]-S[b][c]-S[a][d]+S[a][c]:
                    # print(a,b,c,d,tmp_v,S[b][d],S[b][c],S[a][d],S[a][b])
                    ans = max(ans,(d-c)*(b-a))
                    break
print(ans)
                
