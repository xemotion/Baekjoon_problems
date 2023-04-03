import sys 

read= sys.stdin.readline 



def main(): 

    N = int(read().rstrip()) 
    a = []
    negative = [] 
    positive =[]
    for i in range(N) : 
        val = int(read().rstrip()) 
        if val > 0 : 
            positive.append(val) 
        else: 
            negative.append(val) 
    
    negative.sort() 
    positive.sort() 


   

    if len(a) == 1: 
        print(a[0]) 
    else: 
        sum = 0 
        curr = len(positive) - 1 
        # positive 
        while curr > 0 : 
            # print(sum, curr)
            x, y = positive[i] , positive[i-1] 
            if x* y > x + y : 
                sum +=   x* y 
                curr -= 2    
            else : 
                sum += x
                curr -= 1 

            if curr == 0: 
                sum += positive[curr]
                    
        i = 0 
        if len(negative) == 1: 
            sum += negative[0] 
        else: 
            while i < len(negative) - 1 : 

            # for i in range(len(negative)) : 
                x, y = negative[i] , negative[i+1] 

                if x * y > x+y : 
                    sum += x * y 
                    i += 2
                else: 
                    sum += x 
                    i += 1 
                if i == len(negative) -1 : 
                    sum += negative[i] 
                    break 

        print(sum) 


if __name__ == '__main__':
    main()
    