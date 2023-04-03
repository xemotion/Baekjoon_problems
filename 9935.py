import sys 

read = sys.stdin.readline 


def main() : 

    test_str = read().rstrip() 
    
    explosion = read().rstrip() 
    len_e = len(explosion) 
    stack = [] 
    for i in range(len(test_str)): 
        stack.append(test_str[i]) 
        if ''.join(stack[-len_e:]) == explosion: 
            for _ in range(len_e): 
                stack.pop() 

    if len(stack) == 0: 
        print("FRULA")
    else:      
        print(''.join(stack)) 

    

if __name__ == '__main__':
    main()
    