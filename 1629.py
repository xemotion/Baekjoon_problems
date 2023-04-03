import sys 

read = sys.stdin.readline 
global C 

def divide_multiply(a,b) : 
    global C 

    if b == 0 : 
        return 1
    elif b == 1 :
        return a 

    res = divide_multiply(a, b//2) 

    if b % 2 == 0:
        return (res * res)  % C 
    
    else: 
        return (res * res * a) % C 

        
def main() : 
    global C 
    A,  B , C = map(int,  read().rstrip().split()) 

    result = divide_multiply(A,B) 
    print(result % C) 


if __name__ == '__main__':
    main()
    