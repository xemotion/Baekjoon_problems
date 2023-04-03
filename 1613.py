import sys 
read = sys.stdin.readline 


N, K = map(int, read().rstrip().split()) 
matrix = [ [0] * (N+1) for i in range(N+1)]

for i in range(K): 
    v1, v2 = map(int, read().rstrip().split()) 
    matrix[v1][v2] = -1 
    matrix[v2][v1] = 1 
    
S = int(read().rstrip()) 
result = []
input_list = [] 
for i in range(S): 
    s1, s2 = map(int, read().rstrip().split())  
    input_list.append((s1,s2))

# 순서 정리하기 
for k in range(1,N+1): 
    for i in range(1, N+1) : 
        for j in range(i+1, N+1): 
            if matrix[i][k] == -1 and matrix[k][j] == -1: 
                matrix[i][j] = -1 
                matrix[j][i] = 1
            elif matrix[i][k] == 1 and matrix[k][j] == 1: 
                matrix[i][j] = 1
                matrix[j][i] = -1  

# result 
for i in input_list: 
    print(matrix[i[0]][i[1]]) 

