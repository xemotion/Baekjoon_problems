import sys 
from bisect import bisect_left

read = sys.stdin.readline 


def main(): 

    N = int(read().rstrip()) 
    M = int(read().rstrip()) 

    a = list(map(int, read().rstrip().split()))
    cnt = 0 
    a.sort()
    curr = 0
    idx = len(a) -1 
    while curr < idx:  
        if a[curr] +  a[idx] == M: 
            cnt += 1
            curr += 1
            idx -= 1 

        elif a[curr] +  a[idx] > M: 
            idx -= 1 
        else:  
            curr += 1
        
    
        

    print(cnt) 



if __name__ == "__main__":
    main() 