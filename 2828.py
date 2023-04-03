import sys 

read = sys.stdin.readline 

def main(): 

    N, M = map(int, read().rstrip().split()) 
    K = int(read().rstrip())
    a = [] 
    for i in range(K) :     
        a.append(int(read().rstrip())) 
    min_m = 1 
    max_m = M 
    
    result = 0 
    d = 0
    for i in range(K): 

        if max_m < a[i] : 
            d = a[i]  - max_m

            min_m += d 
            max_m += d
            
        elif min_m > a[i] :
            d = min_m - a[i] 

            min_m = a[i]
            max_m -= d 
            
        else: 
            d = 0 
        # print((min_m, max_m, d))
        result += d 

    print(result) 



if __name__ == '__main__':
    main()
    