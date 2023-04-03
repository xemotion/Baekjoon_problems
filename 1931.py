import sys 

read = sys.stdin.readline 




def main() : 
    N = int(read().rstrip()) 

    meetings = [] 
    for i in range(N): 
        s, e  = map(int, read().rstrip().split())
        meetings.append((s,e, (e-s))) 



    m = sorted(meetings, key = lambda x : (x[1], x[0])) 
    m_max = max(m) 

    cnt = 1 

    s = m[0][0] 
    e = m[0][1] 

    for i in range(1, N): 

        s = m[i][0] 

        if s >= e : 
            cnt += 1        
            e = m[i][1] 
        
        
    print(cnt) 


if __name__ == '__main__':
    main()
    