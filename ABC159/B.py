s = input()
n = len(s)
print('Yes' if s==s[::-1] and s[:(n-1)//2]==s[:(n-1)//2][::-1] and s[(n+1)//2:] == s[(n+1)//2:][::-1] else 'No')