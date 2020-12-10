def sum_array_2D(A):
    h = len(A)
    w = len(A[0])
    S = [[0]*(w+1)]
    for i in range(h):
        tmp = [0]
        for j in range(w):
            tmp.append(tmp[-1]+A[i][j]+S[-1][j+1]-S[i][j])
        S.append(tmp)
    return S