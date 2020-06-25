import collections
S = input()
T = collections.deque([])
for s in S:
    T.append(s)
stack = []
for t in T:
    if not stack:
        stack.append(t)
    else:
        if stack[-1] != t:
            stack.pop()
        else:
            stack.append(t)
print(len(T)-len(stack))
