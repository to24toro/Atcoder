n = int(input())
S = input()
from collections import deque
ans = ''
store = deque([])
i = 0
for i in range(n):
    if len(store)<2:
        store.append(S[i])
    elif S[i]=='x':
        o = store.pop()
        f = store.pop()
        if f=='f' and o=='o':
            continue
        else:
            store.append(f)
            store.append(o)
            store.append(S[i])
    else:
        store.append(S[i])
# print(store)
print(len(store))
# while i<n:
#     if i+3 <n and S[i:i+3]=='fox':
#         i +=3
#     elif i+2 < n and S[i:i+2]=='fo':
#         store.appendleft('fo')
#         i+=2
#     elif S[i]=='f':
#         store.appendleft('f')
#         i+=1
#     elif i+2 < n and S[i:i+2]=='ox':
#         if store and store[0]=='f':
#             store.popleft()
#             i+=2
#         else:
#             store.appendleft('ox')
#             i+=2
#     elif S[i]=='x':
#         if store and store[0]=='fo':
#             store.popleft()
#             i+=1
#         else:
#             store.appendleft('x')
#             i+=1
#     else:
#         store.appendleft(S[i])
#         i+=1
# while store:
#     p =store.pop()
#     ans+=p
# print(len(ans))
