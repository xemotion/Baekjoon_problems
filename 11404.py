import sys 
import math 

read = sys.stdin.readline 

def bfs(): 
    pass 

def print_matrix(matrix): 
    for i in range(len(matrix)) : 
        for j in range(len(matrix)): 
            print(matrix[i][j] , end = ' ')
        print() 
def main(): 
    N = int(read().rstrip()) 
    M = int(read().rstrip()) 


    matrix = [ [ math.inf]  * (N+1) for i in range(N+1) ] 
    
    for _ in range(M): 
        v1, v2, d = map(int,read().rstrip().split()) 
        matrix[v1][v2] = min(matrix[v1][v2], d) 

    
    for i in range(1, N+1) :
        matrix[i][i] = 0 

    # print_matrix(matrix) 

    # matrix[i][j] = min(matrix[i][k] + matrix[k][j], matrix[i][j]) 

    for k in range(1, N+1) : 
        for i in range(1, N+1) : 
            for j in range(1, N+1):  
                if i == j : 
                    matrix[i][j] = 0
                else: 
                    matrix[i][j] = min(matrix[i][k] + matrix[k][j], matrix[i][j])


    # print_matrix(matrix) 
    for i in range(1, N+1): 
        for j in range(1, N+1): 
            if matrix[i][j] == math.inf : 
                print(0, end = ' ')
            else: 
                print(matrix[i][j], end = ' ')
        print() 



    

if __name__ == '__main__':
    main()
    