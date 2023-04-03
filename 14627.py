import sys 

read = sys.stdin.readline 

global pa, M 


def check(mid):
    
    global pa,M 
    cnt = 0 

    for i in pa: 
        # print(i, mid, i//mid, cnt) 
        cnt += (i // mid)
    
    return cnt >= M 


def main() : 
    
    global pa, M 
    N, M = map(int, read().rstrip().split())
    pa = [ ] 
    res = 0 
    for i in range(N) : 
        pa.append(int(read().rstrip()))
    
    lo = 1 
    hi = max(pa)  
    res = 0 
    while lo <= hi:
        mid = (lo+hi) //2

        if check(mid): 
            lo = mid + 1
            res = mid 
        else: 
            hi = mid - 1 
            
    print(sum(pa) - res * M) 


if __name__ == '__main__':
    main()
    