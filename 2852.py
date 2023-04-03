import sys 

read = sys.stdin.readline 

def stringToTime(time): 
    min, sec = map(int, time.split(":")) 
    return (min, sec)  

def timeToString(time): 
    (min, sec) =time 
    return str(min) + ":" + str(sec) 
    

def getDiff(start, end) :
    s1, s2 = map(int, start.split(":"))   
    e1, e2 = map(int, end.split(":")) 
    s = e1 - s1  
    m = e2- s2 
    
    if s < 0:
        s += 60 
        m -= 1 
    return str(s) + ":" + str(m) 
    

def main(): 
    N = int(read().rstrip())
    score = [0, 0 ,0 ] 
    scores = [] 
    times = [] 

    for i in range(N): 
        input = read().rstrip().split() 
        win = input[0] 
        time = input[1] 
        score[int(win)] +=1
        scores.append(score)  
        times.append(time) 


    print(scores) 
    print(times) 
    prev = 0 

    
if __name__ == '__main__':
    main()
    