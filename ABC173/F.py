N = int(input())
#ある頂点がLRに存在する個数とある辺がLRに存在する範囲を求める

ans = 0
for i in range(1,N+1):
    ans += i*(N-i+1) #頂点数*（その頂点数が何個作れるか）
for i in range(N-1):
    u,v = map(int,input().split())
    ans -= min(u,v)*(N+1-max(u,v)) #辺がLRに含まれる個数
print(ans)