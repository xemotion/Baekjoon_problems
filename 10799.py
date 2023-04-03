import sys
read = sys.stdin.readline 


def main(): 
    s_stack = list(read().rstrip())
    cnt, bar_cnt = 0,0 
    curr = s_stack.pop() 
    while len(s_stack) > 0: 
        # print(s_stack) 
        top = s_stack[-1] 
        # laser 
        if curr == ')' and top =='(': 
            cnt += bar_cnt  
        elif curr ==")" and top ==")" : 
            bar_cnt += 1
        elif curr =="(" and top =="(" : 
            cnt += 1 
            bar_cnt -= 1 
        curr = s_stack.pop() 
        
    print(cnt)



if __name__ == '__main__':
    main()
    