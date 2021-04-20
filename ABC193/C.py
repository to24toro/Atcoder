n = int(input())
set_ = set()
for i in range(2,int(n**0.5)+1):
    s = i
    for j in range(2,35):
        s *=i
        if s<=n:
            set_.add(s)
        else:
            break
print(n-len(set_))

