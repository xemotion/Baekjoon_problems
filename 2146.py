import sys 
from collections import deque 
sys.setrecursionlimit(10 ** 6) 


read = sys.stdin.readline 

d = ((1,0), (0,1), (-1,0), (0,-1)) 


global visited, matrix, q, N, b_distance 

def bfs() : 

    global visited, matrix, q, N, res, b_distance
    res = 0
    while len(q) > 0 : 
        r, c, val = q.popleft() 

        
        for dr, dc in d: 
            nr, nc = dr + r , dc + c 
            if nr > N-1 or nr < 0 or nc > N-1 or nc < 0 or visited[nr][nc] != 0 or matrix[nr][nc] == 1 : 
                continue 
                
            if matrix[nr][nc] < 0 and matrix[nr][nc] != val: 
                # print("nr,nc ", matrix[nr][nc], (nr,nc) , val)
                res = visited[r][c] 
                b_distance.append(res-1) 
                return res 

            if matrix[nr][nc] == 0: 
                q.append((nr,nc, val))
                visited[nr][nc] = visited[r][c] + 1 

            # res = visited[nr]

            # print(nr,nc, distance)

    return res - 1 

def dfs(r,c, val): 

    global visited, matrix, q, N, visited_bfs
    visited[r][c] = 1

    for dr, dc in d : 
        nr, nc = dr + r, dc + c 
        if nr > N-1 or nr < 0 or nc > N-1 or nc < 0 or visited[nr][nc] != 0 : 
            continue 

        if matrix[nr][nc] == 0 and matrix[r][c] == 1:
            matrix[r][c] = val 

        if matrix[nr][nc] == 1: 
            dfs(nr,nc,val)


def print_matrix(matrix): 
    for i in range(len(matrix)) : 
        for j in range(len(matrix)): 
            print(matrix[i][j], end =' ')
        print() 

        
def main() : 
    global visited, matrix, q, N, res, b_distance 
    N =  int(read().rstrip()) 

    matrix = [] 
    visited = [ [0] * N for i in range(N)]

    q = deque() 
    b_distance= [ ]

    for i in range(N) : 
        a = list(map(int, read().rstrip().split()))
        matrix.append(a)     

    cnt = 2     
    bridge = [] 
    for i in range(N): 
        for j in range(N): 
            if matrix[i][j] == 1 and visited[i][j] == 0: 
                dfs(i,j, -cnt)
                bridge.append(-cnt) 
                cnt += 1 

    # print_matrix(matrix) 

    visited_bfs = [ [0] * N for i in range(N)]
    
    result  =  N * N + 1
    visited = [ [0] * N for i in range(N)]
    res = 0 
    # 다리 길이 찾기 
    for k in bridge:     
        visited = [ [0] * N for i in range(N)]
        for i in range(N): 
            for j in range(N) : 
                if matrix[i][j] == k and visited[i][j] == 0: 
                    q.append((i,j, k)) 
                    visited[i][j] = 1
                
        
        res = bfs() 
        q.clear() 
        
        # print(res-1, k) 
    # print((b_distance))
    print(min(b_distance)) 
        # result = min(result, res-1) 


    # print(result) 


if __name__ == '__main__':
    main()
    