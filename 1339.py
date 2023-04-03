import sys 

read = sys.stdin.readline 


def main(): 
    global N, matrix, max_len 
    N = int(read().rstrip()) 
    
    result = [ 0 for i in range(10)]
    word_list = [] 
    for i in range(N): 
        word_list.append(read().rstrip()) 

    
    for word in word_list : 
        digits = 1 
        for i in range(len(Word) -1, -1, -1): 
            result[ord[word[i]]]

            digit *= 10 

    result.sort() 


if __name__ == '__main__':
    main()
    