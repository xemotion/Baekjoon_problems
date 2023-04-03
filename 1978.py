import sys 

read = sys.stdin.readline 

global prime_number 

def isPrimeNumber(num): 
    global prime_number 

    if num == 1: return False 
    if num == 2: return True 
    
    for i in prime_number: 
        if num % i == 0:
            return False 
    
    prime_number.append(num) 
    return True 


    

def main(): 
    global prime_number 
    N = int(read().rstrip()) 
    a = list(map(int, read().rstrip().split()))  
    cnt = 0 
    max_num = max(a) 
    for i in range(2, max_num+1):
        for j in a: 
            if j==1 :
                a.remove(j) 
                continue 
            if i != j  and j % i == 0 : 
                a.remove(j) 

    print(len(a))  


if __name__ == '__main__':
    main()
    