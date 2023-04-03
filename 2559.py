import sys 

read = sys.stdin.readline 


def main(): 
    N, K = map(int, read().rstrip().split()) 

    a = list(read()) 

    dp_sum = [ 0 for i in range(N)]
    dp_sum[0] = a[0] 
    if N <= K: 
        print(sum(a))
        return 

    for i in range(1, len(a)) : 
        if i > K-1: 
            dp_sum[i] = dp_sum[i-1] - a[i-K] + a[i] 
        else: 
            dp_sum[i] = dp_sum[i-1] + a[i] 
    # print(dp_sum)
    print(max(dp_sum[K-1:])) 




if __name__ == '__main__':
    main()
    