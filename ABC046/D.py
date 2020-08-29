s = input()
p = 0
g = 0
cnt = 0
for i in s:
    if i =='g':
        if p<g:
            p += 1
            cnt += 1
        else:
            g += 1
    else:
        if p<g:
            p += 1
        else:
            g += 1
            cnt -=1
print(cnt)

