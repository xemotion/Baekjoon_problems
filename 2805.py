import sys 

read = sys.stdin.readline 

global a, M 

def check(mid): 
    global a, M 
    sum = 0  
    for i in a:
        if i <= mid : 
            continue 

        sum += i - mid 
    
    return sum 



def main(): 
    global a, M 
    N, M = map(int, read().rstrip().split()) 

    a = list(map(int, read().rstrip().split())) 

    # mid  = lo 

    lo = 0 
    hi = max(a)
    
    while lo <= hi : 
        mid = (lo + hi ) // 2
        if check(mid) >= M: 
            lo = mid +1 
        else: 
            hi = mid - 1 

        # print(lo, hi, mid, check(mid)) 


    print(hi)

            
            




if __name__ == '__main__':
    main()
    