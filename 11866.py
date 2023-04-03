import sys 
from collections import deque 

read = sys.stdin.readline 


def main(): 
    q = []
    N, K = map(int, read().rstrip().split()) 
    for i in range(1, N+1): 
        q.append(i)

    idx = K - 1
    result =[]
    while len(q) > 0: 
        val = q.pop(idx) 
        result.append(val) 
        idx  += (K - 1) 
        # print(idx, len(q)) 
        if len(q) == 0: 
            break 
        idx = idx % len(q) 

    # print(result)
    print("<", end='') 
    for i in result[:-1]: 
        print(i, end =', ')
    print(result[-1], end =">")


if __name__ == '__main__':
    main()
    