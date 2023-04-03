from bisect import bisect_left
import sys 


read = sys.stdin.readline 

def main() : 
    N = int(read().rstrip()) 
    M = int(read().rstrip()) 
    
    armors = list(map(int , read().rstrip().split()))

    armors.sort()   

    cur = 0
    cnt = 0  
    val = M - armors[0] 
    idx = bisect_left(armors, val)
    
    
    while idx < len(armors) and cur <= idx:
        if armors[idx] == val : 
            cnt+=1
            idx += 1
            cur += 1 

        if armors[idx] < val : 
            idx += 1 
        else: 
            cur += 1
        
    print(cnt) 



if __name__ == "__main__" : 
    main() 