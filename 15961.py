import sys 
read = sys.stdin. readline 


def main(): 
    # N - 초밥수, D 초밥 종류, K - 연속 접시 수, C - 쿠폰 
    N, D , K, C = map(int, read().rstrip().split()) 
    dishes = [] 
    for i in range(N) : 
        dishes.append(int(read().rstrip())) 

    lo = 0 
    category = [ 0 for i in range(D+1)] 


    for i in range(K) : 
        # print(dishes[i], i) 
        category[dishes[i]] += 1
        dishes.append(dishes[i])
        

    kind = D - category.count(0) + 1
    res = [] 
    temp = 0 
    if category[C] == 0:    
        temp = kind + 1 
    else: 
        res.append(kind) 
    # print("kind", kind) 
    

    for i in range(K, N*2 ): 

        # 추가하고 (다음꺼) 
        dishes.append(dishes[i])
        category[dishes[i]] += 1
        # 처음껀 빼야 함 
        category[dishes[lo]] -= 1   

        if category[dishes[lo]] == 0: 
            kind -= 1
        if category[dishes[i]]  == 1: 
            kind += 1

        lo += 1 
        # print(category, lo, i) 

        
        if category[C] == 0:    
            res.append(kind + 1) 
        else: 
            res.append(kind)

    # print(res) 
    print(max(res)) 
    



if __name__ == '__main__':
    main()
    