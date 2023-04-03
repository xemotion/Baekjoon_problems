import sys 
from collections import deque 

read = sys.stdin.readline 
global number, k_list 
number = [] 
result = [] 
global min, max 




# curr -> 검사하는 숫자가 min  - max 사이에 들어가 
def main(): 
    N, K = map(int, read().rstrip().split())
    a = list(map(int, read().rstrip().split()))
    number = list(str(N)) 




if __name__ =="__main__" : 
    main() 