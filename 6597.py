import sys 

read = sys.stdin.readline 

def post_order(pre_order, in_order ): 
    size = len(pre_order)

    # print(pre_order, in_order) 
    if size == 0 :
        return 

    root = pre_order[0]
    left_tree = in_order.index(root) 


    
    # left 
    post_order(pre_order[1:left_tree+1] , in_order[0:left_tree] ) 
    # right 
    post_order(pre_order[left_tree+1:] , in_order[left_tree+1:] ) 
        
    print(root, end ='') 


    
def main() : 
    while True:
        try:
            pre_order, in_order = read().rstrip().split()
            post_order(pre_order, in_order)
            print()
        except:
            break

   
if __name__ == '__main__':
    main()
    