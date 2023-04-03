import sys 
read = sys.stdin.readline 


def main() :    
    S = list(read().rstrip())  
    cnt = 0 
    R = S.copy()

    # print(S) 
    R.reverse() 
    # print(R) 


    for i in range(len(S)) : 
        if S[i:] == R[:len(S) -i ] : 
            cnt = len(S)-i 
            break 

    
    # print(cnt) 

    res = 2* len(S) - cnt 

    print(res) 

if __name__ == "__main__":
    main() 