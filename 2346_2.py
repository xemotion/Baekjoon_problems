import sys 
from collections import deque 

read = sys.stdin.readline

def move_right(val, q): 
    for _ in range(val): 
        q.append(q.popleft()) 
def move_left(val, q): 

    for _ in range(val): 
        q.appendleft(q.pop()) 


def main(): 
    N = int(read().rstrip())

    a = list(map(int, read().rstrip().split()))
    
    q = deque([i for i in range(N)])
    while True: 

        idx = q.popleft() 
        val = a[idx] 

        if len(q) == 0: 
            break 
        if val > 0: 
            move_right(val-1, q) 
        elif val < 0: 
            move_left(-val, q) 

            



if __name__ == '__main__':
    main()
    