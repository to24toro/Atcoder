n=int(input())
l=[]
for i in range(3):
   l.append(int(input()))
for i in range(100):
   if n in l:
      print("NO")
      exit()
   if n-3 in l:
      if n-2 in l:
         if n-1 in l:
            print("NO")
            exit()
         else:
            n-=1
      else:
         n-=2
   else:
      n-=3
   if n<=0:
      print("YES")
      exit()
print("NO")