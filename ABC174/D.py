n = int(input())
l = str(input())
 
r = l.count("R")
print(r - l[:r].count("R"))