import sys 


read = sys.stdin.readline 

def getIndex(a) :
    return ord(a) - ord('a') 


def main() : 
    S = read().rstrip()  
    

    result = [ 0 for i in range(26)] 

    for i in S: 
        result[getIndex(i) ] += 1 

    for i in result: 
        print(i, end = ' ')
    # print(result) 



if __name__ == '__main__':
    main()
    


