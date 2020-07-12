N = int(input())
X = input()
# def division_binary_shift_m(a, b, m):
#     if a < b:
#         return 0
#     if b == 0:
#         raise ZeroDivisionError
#     q = 0
#     sb = b << m
#     print(sb)
#     rem = a
#     while rem >= b:
#         while sb > rem:
#             sb = sb >> 1
#             m = m - 1

#         q = q + (1 << m)
#         rem = rem - sb
#     return rem
# print(division_binary_shift_m(111,10,10))
cnt = 0
for i in X:
    if i=='1': cnt += 1
for i in X:
    if i=='1':
        div = cnt-1
    else:
        div = cnt +1
    print(bin(15)/bin(3))