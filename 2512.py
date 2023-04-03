import sys 

read = sys.stdin.readline  

global budgets, M 
def check(mid):
    global budgets, M 
    sum = 0 
   
    for i in budgets : 
        if i > mid: 
            sum += mid 
        else: 
            sum += i 
    
    return sum 
    


def main(): 
    global budgets, M 
    N = int(read().rstrip()) 
    
    budgets = [] 
    budgets = list(map(int, read().rstrip().split())) 
    M = int(read().rstrip()) 

    lo = 0 
    hi = max(budgets) 

    res = 0 
    while lo <= hi :   

        mid = (lo+hi) // 2
        if check(mid) <= M : 
            lo = mid + 1 
            res = mid
        else: 
            hi = mid - 1 

    
    
    print(res) 


if __name__ == '__main__':
    main()
    