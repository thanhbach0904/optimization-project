#3 steps
#step 1: construct a solution by using greedy method and randomness
#step 2: search for the neighbors of the generated solution and update if a better solution has been found
#step 3: repeat step 1-2 until no more improvement is possible or reach the maximum number of iterations.
import random
#generate X
def GenerateX(x,n,k,c,e,a,b):
    #c is the similarity matrix, the remains are integers, x is empty list
    room = {}
    #từ điển lưu trữ lại số đồ án mỗi phòng
    for i in range(1,k+1):
        room[i] = 0
    complete = True
    for i in range(n):
        #các giá trị khả dĩ có thể gán cho đồ án thứ i
        x_domain = Domain_of_X(x,n,k,c,room,e,b)
        #nếu x_domain hết giá trị để chọn ngẫu nhiên trước khi đến đồ án cuối thì trả về incomplete
        if len(x_domain) == 0 and i <= n-1:
            complete = False
        else:
            chosen_room = random.choice(x_domain)
            room[chosen_room] += 1
            x.append(chosen_room)
    if complete:
        return x
    return None
def Domain_of_X(x,n,k,c,room,e,b):
    option = []
    if len(x) == 0: #if x has no element
        option = [i for i in range(1,k+1)]
    else:
        for i in range(1,k+1):
            if check(x,n,i,c,room,e,b):
                option.append(i)
    return option
def check(x,n,i,c,room,e,b):
    check = True
    thesis = len(x)
    if room[i] >= b:
        check = False
    same_ith_room = []
    for j in range(len(x)):
        if x[j] == i:
            same_ith_room.append(j)
    if len(same_ith_room) != 0:
        for thesis1 in same_ith_room:
            if c[thesis1][thesis] < e:
                check = False
    return check
#Get better X
def GenerateBetterX(x):
    pass
#generate Y
def GenerateY(x,m,k,g,c,d,f,t):
    #x is the list that is being generated first
    #g is the similarity matrix
    #t is the list of supervised teachers. The remains are integers

    pass
def Sum_XY(x,y):
    pass
def Print_Solution(n,m,x,y):
    print(n)
    for i in x:
        print(i,end = ' ')
    print()
    print(m)
    for i in y:
        print(i,end = ' ')

def main():
    #inputs
    N,M,K = map(int,input().split())
    a,b,c,d,e,f = map(int,input().split())
    C = []
    G = []
    for _ in range(N):
        rowC = list(map(int,input().split()))
        C.append(rowC)
    for _ in range(N):
        rowG = list(map(int,input().split()))
        G.append(rowG)
    T = list(map(int,input().split()))
    #run for answer
    iterations = 10
    target_sum = 0
    for i in range(1,iterations):
        x0 = GenerateX([],N,K,C,e,a,b)
        if x0 != None:
            X = GenerateBetterX(x0)
            Y = GenerateY(X,M,K,G,c,d,f,T)
            if Sum_XY(X,Y) > target_sum:
                target_sum = Sum_XY
                Print_Solution(N,M,X,Y)
                print(target_sum)
        #else skip
    

    





if __name__ == '__main__':
    main()
