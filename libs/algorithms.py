import numpy as np


def LCS(A,B):

    n = len(A)
    m = len(B)

    c_table = [[0 for i in range(m+1)] for j in range(n+1)]
    b_table = [[0 for i in range(m)] for j in range(n)]

    for i in range(n):
        ic = i + 1
        for j in range(m):
            jc = j + 1
            #print(i,j)
            if A[i] == B[j]:
                c_table[ic][jc] = c_table[ic-1][jc-1] + 1
                b_table[i][j] = 'd'
            elif c_table[ic-1][jc] >= c_table[ic][jc-1]:
                c_table[ic][jc] = c_table[ic-1][jc]
                b_table[i][j] = 'u'
            else:
                c_table[ic][jc] = c_table[ic][jc-1]
                b_table[i][j] = 'l'

    c_table, b_table = np.array(c_table), np.array(b_table)

    return c_table[-1][-1], b_table


def print_LCS(b,A,i,j):
    
    if b[i][j] == 'd':
        print_LCS(b,A,i-1,j-1)
        print(A[i])
    elif b[i][j]=='u':
        print_LCS(b,A,i-1,j)
    else: 
        print_LCS(b,A,i,j-1)


def calculate_LCS(b,A,n,m):

    i=n-1
    j=m-1
    
    idx = []
    string = []
    while i>=0 and j>=0:
        if b[i][j] == 'd':
            print((i,j),A[i])
            string.append(A[i])
            idx.append(i)
            i -= 1
            j -= 1
        elif b[i][j] == 'u':
            i -= 1
        else:
            j -= 1

    return idx[::-1], string[::-1]








def LIS(A, B):


    n = len(A)

    A_sorted = np.sort(A)
    m = len(A_sorted)

    c_table = [[0 for i in range(m+1)] for j in range(n+1)]
    b_table = [[0 for i in range(m)] for j in range(n)]

    for i in range(n+1):
        for j in range(m):
            if i == 0 or j == 0:
                c_table[i][j] = 0
                #b_table[i][j] = '\'
            elif A[i-1] == A_sorted[j-1]:
                c_table[i][j] = 1 + c_table[i-1][j-1]
                #b_table[i][j] = '\'
            else:
                c_table[i][j] = max(c_table[i-1][j], c_table[i][j-1])
    
    print(np.array(c_table))

    return c_table[-1][-1]