import sys 
from collections import deque 
read = sys.stdin.readline 


def main(): 
    N = int(read().rstrip())   

    q = deque() 
    result = [] 

    for i in range(N): 
        command = read().rstrip().split() 
        print(q) 
        if command[0] =="push": 
            q.append(int(command[1]))

        elif command[0] =="pop" :
            if len(q) > 0 :
                result.append(q.popleft())

            else: 
                result.append(-1) 

        elif command[0] == "front": 
            if len(q) > 0: 
                result.append(q[0]) 
            else: 
                result.append(-1) 
        elif command[0] == "size":   
            result.append(len(q)) 
        elif command[0] == "empty": 
            if len(q) == 0:
                result.append(1)
            else: 
                result.append(0) 
        elif command[0] == "back": 
            if len(q) > 0: 
                result.append(q[-1]) 
            else: 
                result.append(-1) 


    for i in result: 
        print(i) 


if __name__ == '__main__':
    main()
    