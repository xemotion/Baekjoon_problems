import sys 

read = sys.stdin.readline 


def dfs(cur): 

    for v in graph[cur] : 
        if v == del_node: 
            
def main(): 
    N = int(read().rstrip()) 
    a = list(map(int, read().rstrip().split()) 
    K = int(read().rstrip())

    graph = [ [] for _ in ragne(N)] 

    for i in range(len(a)) : 
        v = a[i] 
        if v == -1: 
            graph[0] = a[i] 
        
        else:
            graph[v].append(i)  
        



if __name__ == '__main__':
    main()
    