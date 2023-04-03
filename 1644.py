import sys
import math 


read = sys.stdin.readline 

def is_prime(n): 
    if n < 2: 
        return False 
    for i in range(2, int(n**0.5)+1) : 
        if n % i == 0: 
            return False 
    return True 
    

def main():
    N = int(read().rstrip()) 
    # 소수 구하기

    composite = [False for _ in range(N+1)]
    for i in range(2, int(math.sqrt(N))+1) : 
        if composite[i] : 
            continue 
        for j in range(i * 2, N+1, i) : 
            composite[j] = True 


    prime_list = []  
    for i in range(2, N+1) : 
        if not composite[i] : 
            prime_list.append(i) 
    
    sum, prev, cnt, curr = 0, 0, 0, 0 
    
    
    while True : 
        if sum > N : 
            sum -= prime_list[prev]
            prev += 1
        elif len(prime_list) == curr: 
            break 
        elif sum <= N:

            sum += prime_list[curr] 
            curr +=1 
        
        if sum == N : 
            cnt += 1


                  
    print(cnt) 

if __name__ == '__main__':
    main()
    