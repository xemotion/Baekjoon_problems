import sys 

read =sys.stdin.readline 

def main(): 

    text= list(map(int, read().rstrip()))  
    pattern = [0,0]
    for i in range(len(text)-1) : 
        if text[i]!= text[i+1] : 
            pattern[text[i]] +=1 
    
    pattern[text[-1]] +=1

    # print(pattern)
            
    print(min(pattern[0], pattern[1]))
if __name__=="__main__" : 
    main() 