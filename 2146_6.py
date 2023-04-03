import sys 
from collections import deque   
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

global visited, matrix, N, res, q, visited_bfs 
def bfs(idx) : 
    global visited, matrix, N, res, q, visited_bfs
    # print(idx)
    print(matrix)
    for i in range(N): 
        for j in range(N): 
            if matrix[i][j] == idx and visited_bfs[i][j] == 0: 
                q.append((i,j))
                visited_bfs[i][j] = 1
                 
  
    min_d = 100000000000000
    while len(q) > 0 : 
        r, c  = q.popleft() 
        d = ((1,0), (0,1), (-1, 0), (0,-1))

        for dr, dc in d: 
            nr , nc = dr +r , dc + c 

            if nr > N-1 or nr < 0 or nc > N-1 or nc < 0 or matrix[nr][nc] > 0  or visited_bfs[i][j] !=0: 
                continue 

            # print(idx, matrix[nr][nc], "----->",  visited_bfs[r][c])

            if matrix[nr][nc] != idx and matrix[nr][nc] <0: 
                # print("거리 측정 ", res, visited_bfs[nr][nc])    
                min_d = min(min_d, visited_bfs[r][c])
                res.append(min_d)
                # print(res) 
                return 

            q.append((nr,nc))
            visited_bfs[nr][nc] = visited_bfs[r][c] +1 



def dfs(r, c , cnt): 
    global visited, matrix, N, res, q, visited_bfs 
    
    visited[r][c] = 1

    d = ((1,0), (0,1), (-1, 0), (0,-1))
    for dr, dc in d: 
        nr , nc = dr +r , dc + c 

        if nr > N-1 or nr < 0 or nc > N-1 or nc < 0 or visited[nr][nc] != 0  : 
            continue 

        if matrix[nr][nc] == 1: 
            # print("DFS - ")
            dfs(nr,nc, cnt)

        if matrix[nr][nc] == 0:             
            matrix[r][c] = cnt



def main() : 
    global visited, matrix, N, res, q , visited_bfs

    N = int(read().rstrip() )

    matrix = [] 
    
    visited = [ [0] * N for i in range(N)]
   
    
    for i in range(N): 
        a = list(map(int, read().rstrip().split()))
        matrix.append(a) 
    
    print(matrix) 
    cnt = 1
    q = deque() 
    for i in range(N): 
        for j in range(N): 
            if matrix[i][j] == 1 and visited[i][j]  ==0 : 
                dfs(i,j, -cnt)
                cnt+=1 
    print(cnt) 
    visited_bfs = [ [0] * N for i in range(N)]
    # bfs - traverse 
    res =[]
    for i in range(1, cnt): 
        bfs(-i)
    print(min(res))
   

if __name__ =="__main__" :
    main() 

