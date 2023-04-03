import sys 

read = sys.stdin.readline 


def main(): 


    H, W = map(int, read().rstrip().split()) 
    cnt = -1
    flag = False 
    matrix = [ [-1] * W for i in range(H) ] 

    for i in range(H): 
        a = list(read().rstrip()) 
        # print(a) 
        for j in range(W): 
            if a[j] == 'c' or a[j] == 'C': 
                flag = True 
                cnt = 0      
                matrix[i][j] = 0       
            elif flag == True : 
                cnt+=1  
                matrix[i][j] = cnt 
        flag = False     

    for i in range(H): 
        for j in range(W): 
            print(matrix[i][j], end =' ')
        print() 

    # print(matrix) 


if __name__ == '__main__':
    main()
    