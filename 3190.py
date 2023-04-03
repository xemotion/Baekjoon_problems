import sys
from collections import deque 


read = sys.stdin.readline 

global q, matrix, change_direction, cur_pos, N, snake  
direction = [ (-1, 0), (1,0), (0,-1), (0,1) ]
L = [2,3,1,0]
D = [3,2,0,1] 

def printMatrix(matrix): 
    for i in range(len(matrix)): 
        for j in range(len(matrix)) :
            print(matrix[i][j], end = ' ')
        print() 

def bfs(): 
    # head, tail 
    global q, matrix, snake, change_direction, cur_pos, N  

    timer = 0 
    # current -> snake [ (), () ] 로 표시함 
    # 1. 탈출 조건 - 자신의 몸으로 부딪히거나, 벽에 부딪힐 때, 현재 위치가 뱀의 범위에 속하는가? 머리의 다음 방향이 벽에 부딪히는가? (벽은 0,0, N-1등임)
    # 2. 사과를 먹으면 - 머리만 늘어남, snake 에 좌표 추가 
    # 3. 초 지난 것을 체크하기 위해서는??? 무엇을????? timer 변수를 하나 가지고 가야지 
    # 좌표는 snake 를 돌려야 함 -> 방향은 dr, dc 로 돌림 
    while len(q) > 0 :
        r, c = q.popleft() 
        dr, dc = direction[cur_pos]  
        nr, nc = dr + r, c + dc     
        
        timer += 1 

        if nr > N-1 or nr < 0 or nc > N -1 or nc < 0 : 
            return timer 
 
        if (nr, nc) in snake: 
            return timer 

        if len(change_direction) > 0 and  timer == change_direction[0][0]: 
            t, command = change_direction[0] 
            change_direction.pop(0)
            if command =='D' :
                cur_pos = D[cur_pos]
            elif command =='L': 
                cur_pos = L[cur_pos]

        if matrix[nr][nc] == 1:
            matrix[nr][nc] = 0 
        else: 
            snake.pop() 


        q.append((nr,nc))
        snake.appendleft((nr,nc)) 

    return timer 



def main(): 
    
    global q, matrix, snake, change_direction, cur_pos, N
    N = int(read().rstrip()) 
    K = int(read().rstrip()) 
    matrix = [ [0] * N for i in range(N)]   
    # direction은 오른쪽으로만 향한 (머리가 향하는 쪽을 인식하고 있어야 함 )
    # direction = [ 상,하,좌,우 ] - 0,1,2,3 - 
    # direciton = [ (-1, 0), (1,0), (0,-1), (0,1) ]
    # L = [2,3,1,0]
    # D = [3,2,0,1]
    for i in range(K) : 
        r,c = map(int, read().rstrip().split()) 
        matrix[r-1][c-1] = 1 
    visited = [ [0] * N for i in range(N)]
    # direction information 
    LL = int(read().rstrip())

    change_direction = [] 
    
    for i in range(LL): 
        
        changes = read().rstrip().split() 
        change_direction.append((int(changes[0]), changes[1])) 

    q = deque() 
    snake = deque() 
    # 우 방향으로 시작 
    cur_pos = 3 

    tail = (0,0)
    q.append((0,0)) 
    snake.append((0.0)) 

    res = bfs() 
    print(res) 

if __name__ == '__main__':
    main()
    