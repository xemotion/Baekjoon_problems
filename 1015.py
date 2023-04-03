import sys 

read = sys.stdin.readline 


def main() : 
    N = int(read().rstrip()) 
    A = list(map(int, read().rstrip().split())) 

    
    P = []
    B = [0 for i in range(N)] 

    sorted_a = sorted(A) 
    for i in A: 
        idx = sorted_a.index(i) 
        P.append(sorted_a.index(i))
        sorted_a[idx] = -1 
    
    for i in P: 
        print(i, end =' ') 
if __name__ == '__main__':
    main()
    