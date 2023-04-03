import sys 
from collections import deque 

global q, N, M, matrix, visited 
read = sys.stdin.readline 


def bfs() : 
    global q, N, M, matrix, visited 

    d = ((1,0), (0,1), (0,-1) ,(-1,0)) 
    
    while len(q) > 0 : 
        r, c = q.popleft() 
        
            
        if r == N-1 and c == M-1: 
            return 
        for dr, dc in d : 
            nr , nc = dr + r, dc + c 

            if nr > N - 1 or nr < 0 or nc > M-1 or nc < 0 or matrix[nr][nc] == 0 or visited[nr][nc] != 0  :
                continue 
            

            q.append((nr,nc))
            visited[nr][nc] += visited[r][c] + 1

            
            if nr == N-1 and nc == M-1 :                 
                return  



        
def main() : 
    global q, N, M, matrix, visited 
    N,M = map(int, read().rstrip().split()) 
    
    matrix = [ ]
    visited = [ [0] * M for i in range(N)] 
    for i in range(N) : 
        a = list(map(int, read().rstrip()))
        matrix.append(a) 
        

    q = deque()
    # print(matrix) 
    q.append((0,0))
    visited[0][0] = 1
    bfs() 
    # print(visited) 
    print(visited[N-1][M-1])

if __name__ == '__main__':
    main()
    