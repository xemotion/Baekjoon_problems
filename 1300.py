import sys
read = sys.stdin.readline 


def main(): 
    N = int(read().rstrip()) 
    K = int(read().rstrip()) 

    matrix = [ [0] * N for i in range(N)]
    B = []
    for i in range(1, N+1) : 
        for j in range(1, N+1): 
            # matrix[i-1][j-1] = i * j 
            B.append(i * j)

    B.sort() 
    print(B[K-1])
    

if __name__ == '__main__':
    main()
    