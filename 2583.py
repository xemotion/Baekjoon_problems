import sys 
sys.setrecursionlimit(10 ** 6)

read = sys.stdin.readline 
d = ((0,1), (1,0), (-1,0), (0,-1))


global visited, matrix, N,M, distance 


def dfs(r,c): 
    global visited, matrix, N,M, distance
    visited[r][c] = 1
    distance += 1
    for dr, dc in d: 

        nr, nc = dr + r, dc +c 
        
        if nr  > N-1 or nr < 0 or nc > M-1 or nc < 0 or visited[nr][nc] != 0 or matrix[nr][nc] == 0: 
            continue 
        dfs(nr,nc) 
        


def main() : 
    global visited, matrix, N,M, distance

    M, N, K = map(int, read().rstrip().split()) 
    matrix = [[1] * M for i in range(N)]
    visited = [[0] * M for i in range(N)]
    result = []     
    for i in range(K): 
        x, y, x1, y1 = map(int, read().rstrip().split())
        for i in range(x, x1): 
            for j in range(y, y1): 
                matrix[i][j] = 0     
    
 

    cnt =0 
    distance = 0 
    result = [] 
    for i in range(N): 
        for j in range(M): 
            if matrix[i][j] == 1 and visited[i][j] == 0: 
                dfs(i,j) 
                cnt += 1
                result.append(distance)
                distance = 0 


    result.sort() 
    print(len(result))
    for i in result: 
        print(i, end =' ')

if __name__ == '__main__':
    main()
    