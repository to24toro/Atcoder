n = int(input())
S = input()
cnt = 0
set_ = set()
for val in range(1000):
    val = str(val).zfill(3)
    a =val[0]
    b = val[1]
    c = val[2]
    flag = False
    for i in range(n):
        if S[i]==a and flag == False:
            for j in range(i+1,n):
                if S[j]==b and flag == False:
                    for k in range(j+1,n):
                        if S[k]==c and flag == False: 
                            cnt += 1
                            flag = True
                            break
                    break
            break
print(cnt)