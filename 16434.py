
import sys

read = sys.stdin.readline 


global attack, rooms 


# max 값 
def check(mid): 
    global attack, rooms 

    max_hp = mid 
    init_attack = attack  

    for r in rooms: 
        t, a, h = r 
        
        if t == 1: 
            attack_cnt = h // init_attack 
            if h % init_attack != 0: 
                attack_cnt +=1 

            mid -= a * (attack_cnt -1) 
            if mid <= 0 : 
                return False 
        else: 
            mid = min(mid + h, max_hp) 
            init_attack += a 



    return True 

def main(): 
    
    global attack, rooms 

    N, attack = map(int, read().rstrip().split()) 
    rooms = [] 
    for i in range(N): 
        t, a, h = map(int, read().rstrip().split()) 
        rooms.append((t,a,h))

    lo = 1 
    hi = int(1e18) 
    res = 0 

    while lo <= hi : 
        mid = (lo + hi) // 2 
        
        
        if check(mid) : 
            hi = mid - 1 
            res = mid 
        else: 
            lo = mid + 1
  
        
    print(res) 

if __name__ == '__main__':
    main()
    

