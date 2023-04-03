import sys 
from collections import deque 

read = sys.stdin.readline 
d = ((1,0), (0,1), (-1,0), (0,-1)) 


global N, M, matrix, visited, x2, y2, q
def bfs(): 
    global N, M, matrix, visited, x2, y2, q
  
    cnt = 1

    while True: 
        
        temp = deque() 
    
        while len(q) > 0: 
            r, c = q.popleft() 

            if r == x2-1  and c == y2 - 1 : 
                return cnt 
            
            for dr, dc in d :
                nr, nc = dr + r, dc + c 

                if nr > N-1 or nr <0 or nc  >M -1 or nc < 0 : 
                    continue 

                if visited[nr][nc] != 0:
                    continue 

                if matrix[nr][nc] == '1': 
                    matrix[nr][nc] = '0' 
                    temp.append((nr,nc))
                else: 
                    q.append((nr,nc)) 
                
                visited[nr][nc] = 1 
        
        q = temp 
        cnt+=1 
    return cnt 

def main(): 
    global N, M, matrix, visited, x2, y2, q
    N, M = map(int, read().rstrip().split()) 
    x1, y1, x2, y2 = map(int, read().rstrip().split())  
    
    q = deque() 
    
    matrix = [] 
    visited = [ [0] * M for i in range(N)]
    
    for i in range(N) : 
        a = list(read().rstrip()) 
        matrix.append(a)
        
    q.append((x1-1, y1-1)) 
    visited[x1-1][y1-1] = 1 
    res = bfs() 
    print(res) 
   
def print_matrix(matrix): 
    for i in range(len(matrix)) : 
        for j in range(len(matrix)) : 
            print(matrix[i][j], end =' ') 
        print() 


if __name__ == '__main__':
    main()
    