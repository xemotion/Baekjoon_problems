import sys 

read = sys.stdin.readline 

def check(mid) : 
    global money, M 
    cnt = 0 
    mm = 0 
    for m in money : 
        if mm < m: 
            cnt +=1 
            mm = mid 
        
        mm -= m 

            
    return cnt 


def main(): 
    global money, M 
    N, M = map(int, read().strip().split())
    money = []    

    for i in range(N) : 
        money.append(int(read().rstrip()))


    lo = min(money) 
    hi = sum(money) 

    while lo <= hi: 
        mid = ( lo + hi ) //2
        # 인출 회수가 많으므로 줄여야 함 -> 돈을 더 크게 줘야 함 
        if check(mid) > M :
            lo = mid + 1 
        else: 
            hi = mid - 1 
            ans = mid 
            
    print(ans) 
    

    

    
if __name__ == '__main__':
    main()
    