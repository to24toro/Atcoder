s = input()
ans = ''
set_ = {'a','i','u','e','o'}
for i in s:
    if i not in set_:
        ans += i
print(ans)