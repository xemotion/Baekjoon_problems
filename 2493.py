import sys 
read = sys.stdin.readline 

# 왼큰 수 찾기... 

def main(): 
    N = int(read().rstrip()) 
    a = list(map(int, read().rstrip().split())) 
    stack = [] 
    result = [ 0 for i in range(N)]

    for i in range(N-1, 0, -1): 
        top = a[i] 
        stack.append(i) 

        # 앞에 숫자랑 비교함 
        for j in range(len(stack)): 
            if a[i+1] > stack[-1] : 
                # 찾았으니 나와야지.. 
                stack.pop() 
                result[i] = i+1
                stack.append(i+1)
        
    print(result) 
    






                




if __name__ == '__main__':
    main()
    