import sys 
from itertools import combinations 
from collections import deque 
import copy 



read = sys.stdin.readline 
global safety_zone, N, M, visited, matrix, q, sc 
d = ((1,0), (0,1), (-1,0), (0,-1)) 


def print_matrix(matrix) : 
    for i in range(len(matrix)) : 
        for j in range(len(matrix)) : 
            print(matrix[i][j], end = ' ')
        print() 

def bfs(matrix_map)  : 
    # print("BFS INVOKE ")
    global safety_zone, N, M, visited, matrix, q, sc 
    cnt = 0 

    while len(q)> 0 :       
        r, c = q.popleft() 

        for dr, dc in d : 
            nr, nc = dr + r, dc + c 
            if nr  > N -1 or nr < 0 or nc > M-1 or nc < 0 or visited[nr][nc] != 0: 
                continue 

            if matrix_map[nr][nc] == 1: 
                continue 

            if matrix_map[nr][nc] == 0: 
                # print(cnt) 
                matrix_map[nr][nc] = 2  
                cnt += 1 
                q.append((nr,nc))
                visited[nr][nc] = 1 

    return cnt 



def main() : 

    global safety_zone, N, M, visited, matrix, q, sc 

    N , M = map(int, read().rstrip().split()) 
    matrix = [] 
    visited = [ [0] * M for i in range(N) ] 
    q = deque() 
    qs = deque() 

    safety_zone =[] 
    virus_loc = [] 

    for i in range(N): 
        a = list(map(int, read().rstrip().split())) 
        matrix.append(a) 
        for j in range(M): 
            if matrix[i][j] == 0: 
                safety_zone.append((i,j))

            if matrix[i][j] == 2: 
                virus_loc.append((i,j))



    result =[] 
    sc = len(safety_zone)
    wall_list = list(combinations(range(0, sc), 3)) 
    res = 100000000
    for walls in wall_list: 
        q = deque() 
        #  q clear 
        for i in virus_loc: 
            q.append(i)
            visited[i[0]][i[1]] = 1 

        sc = len(safety_zone) 
        matrix_map = copy.deepcopy(matrix) 

        visited = [ [0] * M for i in range(N) ] 
        for wall in walls: 
            (x, y)= safety_zone[wall] 

            matrix_map[x][y] = 1 
      
        cnt = bfs(matrix_map) 
        res = min(cnt, res) 
    # print(res) 

    print(sc - res - 3) 

        # print_matrix(matrix_map) 
    # print(result)           
    # print(max(result)) 

    
    



    



if __name__ == '__main__':
    main()
    