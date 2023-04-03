import sys 
from collections import deque 

read = sys.stdin.readline 



def main(): 
    N, K = map(int, read().rstrip().split())
    q = []

    for i in range(1, N+1) : 
        q.append(i)    

    idx = K-1
    print("<", end='')

    while len(q) > 0:         
        q.pop(idx) 
        print(q.pop(idx), end =', ')
        idx = (idx + K) % len(q)
        # print("idx" , idx, len(q), q)
    
    # print(q.pop(), end='>') 


if __name__ =="__main__" : 
    main() 