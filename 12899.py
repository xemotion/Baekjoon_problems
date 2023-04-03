import sys 
import heapq 
read = sys.stdin.readline 


def main(): 
    N = int(read().rstrip()) 
    S = [] 
    result =[] 
    for i in range(N): 
        q, v = map(int, read().rstrip().split()) 

        if q == 1:
            heapq.heappush(S, v) 
            # S.append(v) 
        else:
            S.sort() 
            result.append(S[v-1]) 
            r = S.remove(S[v-1])
            # print(r) 
            


    for i in result : 
        print(i) 
        





            



if __name__ == '__main__':
    main()
    