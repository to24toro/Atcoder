n = int(input())
set_ = set()
l = []
cnt = -1
dic = {}
x = '123456'
def swap(x,i):
    x = [str(i) for i in x]
    x[i%5],x[i%5+1] = x[i%5+1],x[i%5]
    return ''.join(x)
# x = swap(x,0)
# print(x)

while x not in set_ and cnt <n:
    set_.add(x)
    l.append(x)
    cnt += 1
    dic[x] = cnt
    x = swap(x,cnt)
    
if cnt ==n:
    print(l[-1]);exit()

L = l+l
cnt = len(l)
n-=dic[x]
print(l[n%cnt])