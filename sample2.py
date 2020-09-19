# import collections
# import statistics
# n, q = map(int, input().split())
# dic = collections.defaultdict(list)
# set_ = set()
# for _ in range(n):
#     i, x, s, t = input().split()
#     if i in set_:
#         continue
#     dic[x].append((i,s,t))
#     set_.add(i)
# res = []
# for _ in range(q):
#     a, b = input().split()
#     cnt = 0
#     if a not in dic:
#         continue
#     for idx,s,t in dic[a]:
#         if s <=b and b<=t:
#             cnt += 1
#     res.append(cnt)
# print(min(res),max(res),statistics.mode(res),statistics.median(res))


#MaximumLikelihoodEstimation

# print(1024*0.8*0.7*0.9*0.3*0.8*0.15*0.75*0.3*0.85*0.25)
print(1.6*1.4*1.8*0.6*1.6*0.3*1.5*0.5*0.6*1.7)
print(((0.5)**4)*((1.5)**6))

#f1**4*(2-f1)**6

#4f1**3*(2-f1)**6-6*f1**4*(2-f1)**5=0
#(2f1**3*(2-f1)**5)*(4-2f1-3f1)=0
#f1 = 4/5,f2 = 6/5
print(((0.8)**4)*((1.2)**6))

#分母
bunbo=(0.4*0.05+0.3*0.04+0.2*0.03+0.1*0.02)
print(0.2*0.03/bunbo)

#fx = 3x^2+2x+3y=0
#fy =  3y^2 + 2y + 3x=0
#fxx = 6x+2
#fyy = 6y+2
#fxy = 3
#(3x+3y-1)(x-y)=0
#x = -5/3,0
#f = 2x^3+5x^2
print(125/27)

ans = ['0','10','1','100','11']
ans.sort()
print(ans)