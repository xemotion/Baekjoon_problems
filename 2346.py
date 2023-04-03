import sys 
from collections import deque 

read = sys.stdin.readline 

def move_right(val, q): 
    for _ in range(val): 
        q.append(q.popleft()) 


def move_left(val, q ): 
    for _ in range(val): 
        q.appendleft(q.pop())


def main(): 

    N= int(read().rstrip()) 

    a = list(map(int, read().rstrip().split())) 
    
    q = deque([i for i in range(N)]) 

    
    while len(q) > 0: 
        idx = q.popleft() 
        val  = a[idx] 
        print(idx + 1, end = ' ')

        if val > 0 : 
            val -= 1 

        q.rotate(-val) 



if __name__ == '__main__':
    main()
    