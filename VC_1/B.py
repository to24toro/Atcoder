S = input()
two = 0
five = 0
if S.count('2')!=S.count("5"):
    print(-1);exit()
ans = 0
for s in S:
    if s=="2":
        two+=1
    else:
        five+=1
    if five>two:
        print(-1);exit()
    ans = max(ans,two-five)
print(ans)