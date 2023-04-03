import sys 


read = sys.stdin.readline 

global money, N,M 
def check(mid):
    global money, N,M 
    total = mid 
    cnt = 0 
    for i in money : 
        if i > mid: 
            return False 
        
        if i > total : 
            total = mid 
            cnt += 1
            total -= 1
        else: 
            total -= i 

    return cnt <= M 


def main(): 
    global money, N,M 
    N, M = map(int, read().rstrip().split())
    money = []  
    for i in range(N): 
        money.append(int(read().rstrip()))

    lo = 0 
    hi = sum(money) 
    res = 0 
    while lo <= hi:
        mid = (lo + hi ) // 2 

        if check(mid) : 
            hi = mid - 1 
            res = mid 

        else: 
            lo = mid + 1
    print(res) 

            

if __name__ == '__main__':
    main()
    