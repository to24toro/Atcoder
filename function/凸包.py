# #グラハム走査
# #https://qiita.com/kkttm530/items/d6ca372491b75baeac3c

# def signed_area(p1,p2,p3):
#     area = ((p2[0]-p1[0])*(p3[1]-p1[1]))-((p3[0]-p1[0])*(p2[1]-p1[1]))
#     return area

# def convex_hull(p_list):

#     p_sort = []
#     for p in p_list:
#         p_sort.append(p[0])
    
#     min_index = p_sort.index(min(p_sort))
#     min_p = p_list.pop(min_index)
#     p_list.insert(0,min_p)

#     p_length = len(p_list)
#     count = 0
#     index = 0
#     while True:
#         count += 1
#         index += 1

#         area = signed_area(p_list[0],p_list[index],p_list[index+1])

#         if area<0:
#             p_list[index],p_list[index+1] = p_list[index+1],p_list[index]
#             count = 0

#         if count == p_length-1:
#             break

#         if index == p_length-2:
#             index = 0
#     count = 0
#     index = -1
#     while True:
#         count += 1
#         index += 1

#         area = signed_area(p_list[index],p_list[index+1],p_list[index+2])

#         if area<0:
#             del p_list[index+1]
#             count = 0

#         if count == len(p_list):
#             break

#         if index == len(p_list)-3:
#             index = -1
#     return p_list
def det(A, B):
    return A[0] * B[1] - A[1] * B[0]
def vec(A, B):
    return (B[0] - A[0] , B[1] - A[1])

def convexHull(node):
	node.sort()
	chSize = 0
	N = len(node)
	ch = []
	for i in range(N):
		while chSize > 1:
			v_cur = vec(ch[-2], ch[-1])
			v_new = vec(ch[-2] , node[i])
			if det(v_cur, v_new) > 0:
				break
			chSize -= 1
			ch.pop()
		ch.append(node[i])
		chSize += 1
 
	t = chSize
	for i in range(N - 2, -1, -1):
		while chSize > t:
			v_cur = vec(ch[-2], ch[-1])
			v_new = vec(ch[-2] , node[i])
			if det(v_cur, v_new) > 0:
				break
			chSize -= 1
			ch.pop()
		ch.append(node[i])
		chSize += 1
 
	return ch[:-1]