import sys 

read = sys.stdin.readline 


global fibonacci 


def main(): 
    global fibonacci 
    N = int(read().rstrip())

    fibo = [ 0 for i in range(N+2)] 
    fibo[0] = 0 
    fibo[1] = 1

    for i in range(2, N+1): 
        fibo[i] = fibo[i-1] + fibo[i-2]

    print(fibo[N])

    


    
if __name__ == '__main__':
    main()
    