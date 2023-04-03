import sys 

read = sys.stdin.readline 
sys.setrecursionlimit(10**6)
global matrix, visited, N, M 
d = ((1,0), (0,1), (-1,0),(0,-1))

def dfs(r,c ) : 
    global matrix, visited, N, M 

    visited[r][c] = 1 
    for dr, dc in d: 
        nr, nc = dr+r, dc + c 

        if nr > N-1 or nr < 0 or nc > M-1 or nc < 0 or visited[nr][nc] != 0 : 
            continue 

        if matrix[nr][nc] == 1: 
            dfs(nr,nc) 


def main() :
    global matrix, visited, N, M 
 
    T = int(read().rstrip()) 
    result = [] 


    for i in range(T): 
            
        M, N , K = map(int, read().rstrip().split())

        matrix = [[0] * M for i in range(N)] 
        # print(M, N, K)
        for i in range(K) : 
            y, x  = map(int, read().rstrip().split()) 
            matrix[x][y] = 1 
    

        visited = [ [0] * M for i in range(N)] 

        # print(matrix) 


        cnt = 0 

        for i in range(N) : 
            for j in range(M): 
                if matrix[i][j] == 1 and visited[i][j] == 0 : 
                    dfs(i,j)
                    cnt+=1 

        result.append(cnt) 

    for i in result: 
        print(i) 



if __name__ == "__main__": 
    main() 