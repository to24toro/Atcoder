n = int(input())

for i in range(1,40):
    for j in range(1,30):
        if 3**i + 5**j ==n:
            print(i,j);exit()
print(-1)