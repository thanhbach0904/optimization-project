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
    return x
#generate Y
def checkY(x,y,i,teacher_dict,m,k,g,c,d,f,t):
    check = True
    teacher = len(y)
    #a room can only contains up to d teachers
    if teacher_dict[i] >= d:
        check = False
    #similarity between theses and teachers in the same room
    same_ith_room = []
    for j in range(len(x)):
        if x[j] == i:
            same_ith_room.append(j)
    for thesis in same_ith_room:
        if g[thesis][teacher] < f:
            check = False
    #teacher can't be in the same room with their thesis
    return check
def Domain_of_Y(x,y,teachers_in_room,m,k,g,c,d,f,t):
    option = []
    for i in range(1,k+1):
        if checkY(x,y,i,teachers_in_room,m,k,g,c,d,f,t):
            option.append(i)
    return option
def getSum(k,teacher,x,g):
    #g is the similarity matrix
    s = 0
    for i in range(len(x)):
        if x[i] == k:
            s += g[i][teacher]
    return s
        
def GenerateY(x,m,k,g,c,d,f,t):
    #x is the list that is being generated first
    #g is the similarity matrix
    #t is the list of supervised teachers. The remains are integers
    #first we priotize the room that has the least theses, don't care about the target function
    #once all the room has over c theses, we start to focus on the target function
    sum = 0
    teachers_in_room = {}
    for i in range(1,k+1):
        teachers_in_room[i] = 0
    y = []
    complete = True
    for i in range(m):
        y_domain = Domain_of_Y(x,y,teachers_in_room,m,k,g,c,d,f,t)
        if len(y_domain) == 0 and i <= m -1:
            complete = False
        else:
            best_option = []
            for room in y_domain:
                best_option.append((room,teachers_in_room[room]))
            best_option = sorted(best_option,key = lambda x : x[1])
            room_for_teacher = best_option[0][0]
            expectsum = getSum(room_for_teacher,i,x,g)
            teachers_in_room[best_option[0][0]] += 1
            for room1 in range(1,len(best_option)):
                if getSum(room1,i,x,g) > expectsum :
                    teachers_in_room[room_for_teacher] -= 1
                    room_for_teacher = room1
                    teachers_in_room[room1] +=1
                    expectsum = getSum(room1,i,x,g)
            sum += expectsum
            y.append(room_for_teacher)
    if complete:
        return y,sum
    return None
def Sum_XY(k,x,alpha,c):
    #c is the similarity matrix
    sum = 0
    for room in range(1,k+1):
        same_room = []
        for index in range(len(x)):
            if x[index] == k:
                same_room.append(index)
        for thesis1 in range(len(same_room)):
            for thesis2 in range(thesis1 + 1,len(same_room)):
                sum += c[same_room[thesis1]][same_room[thesis2]]
    return sum + alpha

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
    iterations = 100
    target_sum = 0
    finalX = []
    finalY = []
    for i in range(1,iterations):
        x0 = GenerateX([],N,K,C,e,a,b)
        if x0 != None:
            X = GenerateBetterX(x0)
            Y,sumY = GenerateY(X,M,K,G,c,d,f,T)
            if  Y != None:
                if Sum_XY(K,X,sumY,C) > target_sum:
                    target_sum = Sum_XY(K,X,sumY,C)
                    finalX = X
                    finalY = Y
        #else skip
    Print_Solution(N,M,finalX,finalY)
    print()
    print(Sum_XY(K,X,0,C))

    





if __name__ == '__main__':
    main()
