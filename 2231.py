import sys 

read = sys.stdin.readline 

def main(): 
    N = int(read().rstrip())

    
    for i in range(1, N+1): 
        num = sum((map(int, str(i))))
        num_sum = i + num 

        if num_sum == N : 
            print(i) 
            break 
        if i == N : 
            print(0) 
            
if __name__ == '__main__':
    main()
    