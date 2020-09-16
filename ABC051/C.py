sx,sy,tx,ty = map(int,input().split())
a = 'U'*abs(ty-sy)
b = 'R'*abs(tx-sx)
c = 'D'*abs(ty-sy)
d = 'L'*abs(tx-sx)
ans =''
ans += a+b+c+d
ans +='D'
ans +=b+'R'
ans += a + 'U'+'L'
ans += 'U'
ans +=d+'L'
ans += c +'D'+'R'
print(ans)