import sys 
from collections import deque 
from itertools import combinations, permutations 

read = sys.stdin.readline 

global matrix, visited, q, N, M, bags, item_cnt
d = ((1,0), (0,1), (0,-1), (-1,0))

def bfs(): 
    
    global matrix, visited, q, N, M, res 
    while len(q) > 0 : 
        r, c, bit , step= q.popleft() 

        if step < res : 
            for dr, dc in d : 
                    nr, nc = dr +r, dc + c 
                    if nr > N-1 or nr < 0 or nc > M-1 or nc < 0 or matrix[nr][nc] == '#':
                        continue 
                            
                    q.append((nr,nc, bit, step+1)) 
                    visited[nr][nc] = max(visited[r][c] +1, visited[nr][nc]) 

                    
                    if matrix[nr][nc] == 'E' and item_cnt == 0: 
                        res = step 
                        return visited[nr][nc] 




def print_matrix(matrix) : 
    for i in range(len(matrix)): 
        for j in range(len(matrix[0])) : 
            print(matrix[i][j], end =' ')
        print() 


def main() : 
    
    global matrix, visited, q, N, M, bags, item_cnt
    M, N = map(int, read().rstrip().split()) 
    matrix = [] 
    x, y = 0, 0 
    item_pos = [] 
    for i in range(N): 
        a = list(read().rstrip()) 
        matrix.append(a) 
        for j in range(M): 
            if matrix[i][j] == 'S': 
                x, y = i, j 
            if matrix[i][j] =='X': 
                item_pos.append((i,j)) 

    #  start - 
    #  item position 배열 - item_pos 

    q = deque() 
    visited = [ [[0 for _ in range(35)] for  _ in range(M)] for _ in range(N) ] 

    q.append((x, y, 0, 0))
    visited[x][y][0] = 1 

    bfs() 




if __name__ == '__main__':
    main()
    