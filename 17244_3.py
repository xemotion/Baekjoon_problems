import sys 
from collections import deque 

read = sys.stdin.readline 

global matrix, visited, q, N, M, bags, item_cnt
d = ((1,0), (0,1), (0,-1), (-1,0))

def bfs(): 
    
    global matrix, visited, q, N, M, bags, item_cnt
    while len(q) > 0 : 
        r, c, x = q.popleft() 

        for dr, dc in d : 
            nr, nc = dr +r, dc + c 
            if nr > N-1 or nr < 0 or nc > M-1 or nc < 0 or matrix[nr][nc] == '#':
                continue 
            
            # x 를 집은 경우 
            if matrix[nr][nc] == '.' and visited[nr][nc][x] == 0: 
                q.append((nr,nc,x))
                visited[nr][nc][x] = visited[r][c][x] + 1
            elif matrix[nr][nc] == 'X' and x!=0 and visited[nr][nc][x-1] == 0 : 
                q.append((nr,nc,x-1))
                visited[nr][nc][x-1] = max(visited[r][c][x] + 1, visited[nr][nc][x-1]) 
            
            print(visited) 
            print("---------------------------------------")

            if matrix[nr][nc] == 'E' and visited[nr][nc][0] == 0  : 
    
                return visited[nr][nc][0] 


def print_matrix(matrix) : 
    for i in range(len(matrix)): 
        for j in range(len(matrix[0])) : 
            print(matrix[i][j], end =' ')
        print() 


def main() : 
    
    global matrix, visited, q, N, M, bags, item_cnt
    M, N = map(int, read().rstrip().split()) 
    matrix = [] 
  
    q = deque() 
    K = 0 
    x, y = 0, 0 
    for i in range(N): 
        a = list(read().rstrip()) 
        matrix.append(a) 
        print(a) 

        for j in range(M): 
            if matrix[i][j] == 'S': 
                x, y  = i, j 
            if matrix[i][j] =='X': 
                K += 1 
        
    # print(matrix) 
    visited = [ [[0 for i in range(K+1)] for _ in range(M)] for _ in range(N) ] 
    q.append((x,y,K))
    visited[x][y][K] = 1 
    res = bfs()
    
    print_matrix(visited) 
    print(res) 

if __name__ == '__main__':
    main()
    