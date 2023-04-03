from collections import deque 

global q, N, M, matrix, visited, L, res 
# 상하좌우 - 0,1,2,3
direct = [(-1,0), (1,0), (0,-1), (0,1)]
d = [[], [0,1,2,3], [0,1],[2,3], [0,3],[1,3],[1,2],[0,2]] 

# 상 -> 하 
# 하 -> 상 
# 좌 -> 우 
# 우 -> 좌 
conv = [1,0,3,2] 

def bfs() : 
    
    global q, N, M, matrix, visited, L, res 

    while len(q) > 0 :
        r,c = q.popleft() 

        num = matrix[r][c] 
        if visited[r][c] == L : 
            return res 

        for direct_d in d[num]: 
            dr , dc = direct[direct_d] 

            nr, nc = dr + r, dc + c 

            if nr > N- 1 or nr < 0 or nc > M-1 or nc < 0 or visited[nr][nc] != 0 or matrix[nr][nc] == 0:
                continue 
            
            # 갈 곳이 d에서 올 때 갈 수 있는 방향인지 체크해야 함 
             
            if conv[direct_d] not in d[matrix[nr][nc]] : 
               
                continue 
                
            q.append((nr, nc)) 
            visited[nr][nc] += visited[r][c] + 1 
            res += 1 

    return res 

                
def main(): 
    global q, N, M, matrix, visited, L, res 


    T = int(input()) 
    result = [] 
    for t in range(T): 
        N, M, R,C, L = map(int, input().split()) 
        matrix = [] 
        visited =[ [0] * M for i in range(N)]
        q = deque() 

        for i in range(N) : 
            a = list(map(int, input().split())) 
            matrix.append(a) 
      

        q.append((R,C))
        visited[R][C] = 1 
        res = 1 
        bfs() 

        # print(res)
        result.append(res) 

    for i in range(len(result)): 
        print("#"+str(i+1), result[i])



    


if __name__ == '__main__':
    main()
    