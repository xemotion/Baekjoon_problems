import sys 
sys.setrecursionlimit(10**6) 

read = sys.stdin.readline 

global matrix, visited, N 
d = ((-1,0), (0,-1),(0,1), (1,0)) 

def dfs(r,c) : 
    global matrix, visited, N 

    visited[r][c] = 1 
    
    for dr, dc in d : 
        nr , nc = dr + r, dc + c 
        if nr > N-1 or nr < 0 or nc > N -1 or nc < 0 or visited[nr][nc] != 0 or matrix[nr][nc] == 0:
            continue 

        dfs(nr,nc)

def main() : 
    global matrix, visited, N 
    N = int(read().rstrip()) 
    matrix_in = [] 
    rains = set() 
    for i in range(N): 
        a = list(map(int, read().rstrip().split()))  
        matrix_in.append(a) 
        rains.update(set(a.copy())) 

    # print(rains) 
    rains = list(rains) 
    # print(min(rains), max(rains), rains[:-1])
    
    
    result = [1] 
    # matrix =[] 
    for r in rains : 
        # print("rain high ", r) 
        matrix = matrix_in.copy() 
        visited = [ [0] * N for i in range(N)]
        for i in range(N): 
            for j in range(N) : 
                if matrix[i][j] <= r:   
                    matrix[i][j] = 0 

        # print(matrix) 

        cnt = 0 
        for i in range(N): 
            for j in range(N) : 
                if matrix[i][j] != 0 and visited[i][j] == 0: 
                    dfs(i,j)
                    cnt += 1
        result.append(cnt) 
        
        # print("r", r, "--->", cnt)
    # print(result) 
    print(max(result))
    # matrix 에 기준 이하의 값은 0으로 표시를 한다. 그리고 dfs로 영역의 개수를 구함 
if __name__ == '__main__':
    main()
    