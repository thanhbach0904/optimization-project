
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

X = [0 for i in range(N)]
Y = [0 for i in range(M)]

max_G = 0
for g in G:
    for value in g:
        if value > max_G:
            max_G = value
similarity_sum = 0
max_sum = 0


#liệt kê các giá trị khả dĩ của X
all_possible_X = []
def check_X(k,i):
    check = True
    for index in range(i):
        if X[index] == X[i] and C[i][index] < e:
            check = False
    return check

def final_check_X():
    check = True
    for k in range(1, K+1):
        number_of_thesis_in_kth_room = 0
        for i in range(N):
            if X[i] == k:
                number_of_thesis_in_kth_room += 1
        if number_of_thesis_in_kth_room < a or number_of_thesis_in_kth_room > b :
            check = False
    return check

def Solution_X(l):
    l.append(list(X))
    
    
def Try_X(i):
    if i == N:
        if final_check_X():
            Solution_X(all_possible_X)  
        return

    for k in range(1, K+1):
        if check_X(k, i):
            X[i] = k
            Try_X(i + 1)
            



#sau khi có X thì ta sẽ liệt kê Y tương ứng với từng X
final_solution = []
def final_final_check(x,y): #điều kiện đồ án không được chung phòng với giáo viên hướng dẫn 
    check = True
    for i in range(N):
        if x[i]==y[T[i]-1]:
            check = False
            break
    return check
def Final_Solution(x,l):
    global similarity_sum,max_sum
    if [x,list(Y)] not in l and final_final_check(x,list(Y)):
        l.append([x,list(Y)])
    if similarity_sum > max_sum:
        max_sum = similarity_sum
        print(max_sum)
def check_Y(x,k,j):
    check = True
    for index_X in range(len(x)):
        if Y[j] == x[index_X] and G[index_X][j] < f:
            check = False
        
    for index_X in range(len(x)):
        if x[index_X] == k and T[index_X]-1 == j:
            check = False 
    #nếu bỏ đoạn trên đi thì code sẽ chạy mãi không dừng, còn nếu để lại thì nó sẽ cho cả những kết quả thỏa mãn lẫn không thỏa mãn điều kiện của T(i)
    return check

def final_check_Y():
    check = True
    for k in range(1,K+1):
        number_of_teachers_in_kth_room = 0
        for j in range(M):
            if Y[j] == k:
                number_of_teachers_in_kth_room += 1
        if number_of_teachers_in_kth_room < c or number_of_teachers_in_kth_room > d:
            check = False
    return check

def Sum_X(x):
    sum = 0
    for k in range(1,K+1):
        thesis_in_kth_room = []
        for i in range(N):
            if x[i] == k:
                thesis_in_kth_room.append(i)
        for index in range(len(thesis_in_kth_room)):
            for index1 in range(index+1,len(thesis_in_kth_room)):
                sum += C[thesis_in_kth_room[index]][thesis_in_kth_room[index1]]
    return sum
def Sum_kth_Y(j,k,x):
    sum = 0
    thesis_in_kth_room = []
    for k in range(1,K+1):
        thesis_in_kth_room = []
        for i in range(N):
            if x[i] == k:
                thesis_in_kth_room.append(i)
    for thesis in thesis_in_kth_room:
        sum += G[thesis][j]
    return sum



def Try_Y(j):
    global final_solution,all_possible_X,max_sum,similarity_sum

    for k in range(1, K+1):
        for x in all_possible_X:
            similarity_sum = Sum_X(x)
            if check_Y(x, k, j):
                Y[j] = k
                similarity_sum = similarity_sum + Sum_kth_Y(j,k,x)
                if j == M-1:
                    if final_check_Y():
                        Final_Solution(x,final_solution)
                else:
                    estimate_sum = similarity_sum + (M-k+1)*N*max_G
                    if estimate_sum > max_sum:
                        Try_Y(j+1)
                similarity_sum = similarity_sum - Sum_kth_Y(j,k,x)


Try_X(0)          
Try_Y(0)




#tạo hàm tính tổng cần tối ưu
def Calculate_sum(x,y):
    sum = 0
    for k in range(1,K+1):
        thesis_in_kth_room = []
        teachers_in_kth_room = []
        for i in range(N):
            if x[i] == k:
                thesis_in_kth_room.append(i)
        for j in range(M):
            if y[j] == k:
                teachers_in_kth_room.append(j)
        for index in range(len(thesis_in_kth_room)):
            for index1 in range(index,len(thesis_in_kth_room)):
                sum += C[thesis_in_kth_room[index]][thesis_in_kth_room[index1]]
        for teachers in teachers_in_kth_room:
            for thesis in thesis_in_kth_room:
                sum += G[thesis][teachers]
    return sum
    


for x,y in final_solution:
    print(x,y)
    print()

#vẫn đang có vài chỗ thắc mắc












    
        
        
    
