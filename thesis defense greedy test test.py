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

def Sum_X(x,k_thesis,room):
    sum = 0
    x[k_thesis] = room
    for k in range(1,K+1):
        thesis_in_kth_room = []
        for i in range(k_thesis+1):
            if x[i] == k:
                thesis_in_kth_room.append(i)
        if len(thesis_in_kth_room) >= 2:
            for index in range(len(thesis_in_kth_room)):
                for index1 in range(index+1,len(thesis_in_kth_room)):
                    sum += C[thesis_in_kth_room[index]][thesis_in_kth_room[index1]]
    x[k_thesis] = 0
    return sum

def check(x,index,k):
    check_variable = True
    for i in range(index):
        if x[i] == k and C[i][k] < e:
            check_variable = False
    return check_variable


#xét k trường hợp của X có thể từ X1 -> Xk trong đó Xi[0] = i
allX = []
for i in range(K):
    X[0] = i+1
    allX.append(list(X))
#tạo từ điển để theo dõi số lần xuất hiện của một phòng
count = {}
for i in range(K):
    count[i+1] = 0
for X_ in allX:
    count1 = count
    count1[X_[0]] = 1
    SumX = 0
    
    #gán đồ án thứ k vào phòng trong room_domain sao cho Sum_X lớn nhất
    for kth_thesis in range(1,N):
        #room domain là danh sách các phòng có thể chọn được dựa trên số lần xuất hiện
        #nếu phòng nào xuất hiện quá b lần thì sẽ loại khỏi room domain
        room_domain = []
        chosen_room = None
        for room in count1.keys():
            if count1[room] < b:
                room_domain.append(room)
        for room in room_domain:
            if  check(X_,kth_thesis,room):
                if Sum_X(X_,kth_thesis,room) > SumX:
                    chosen_room = room
                    SumX = Sum_X(X_,kth_thesis,room)
        X_[kth_thesis] = chosen_room
        count[chosen_room] +=1
    print(list(X_))
