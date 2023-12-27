from ortools.sat.python import cp_model
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

#khởi tạo model
model = cp_model.CpModel()
x = [] #bool matrix for theses
X = [0]*N

for i in range (N):
    t = []
    for j in range(K):
        t.append(model.NewIntVar(0,1,'x[' + str(i) + ',' + str(j) + ']'))
    x.append(t)

#bool matrix for teachers
y = [] 
Y = [0]*M
for i in range (M):
    t = []
    for j in range(K):
        t.append(model.NewIntVar(0,1,'y[' + str(i) + ',' + str(j) + ']'))
    y.append(t)

#mỗi đồ án chỉ được đưa vào 1 phòng
for i in range(N):
    model.Add(sum([x[i][j] for j in range(K)]) == 1 )
#mỗi giáo viên chỉ ở 1 phòng
    for i in range(M):
        model.Add(sum([y[i][j] for j in range(K)]) == 1 )
#mỗi phòng chỉ có a đến b đồ án
for j in range(K):
    model.Add(sum(x[i][j] for i in range(N)) >= a)
    model.Add(sum(x[i][j] for i in range(N)) <= b)
#mỗi phòng chỉ có c đến d giáo viên
for j in range(K):
    model.Add(sum(y[i][j] for i in range(M)) >= c)
    model.Add(sum(y[i][j] for i in range(M)) <= d) 
#độ tương đồng giữa các đồ án trong cùng 1 phòng phải lớn hơn e
for k in range(K):
    for i in range(N-1):
        for j in range(i+1,N):
            b = model.NewBoolVar('b')
            model.Add(x[i][k]==x[j][k]==1).OnlyEnforceIf(b)
            model.Add(C[i][j] >= e).OnlyEnforceIf(b)



#độ tương đồng giữa giáo viên và đồ án trong cùng một phòng phải lớn hơn f
for k in range(K):
    for j in range(M):
        for i in range(N):
            b = model.NewBoolVar('b')
            model.Add(y[j][k]==x[i][k]==1).OnlyEnforceIf(b)
            model.Add(G[i][j] >= f).OnlyEnforceIf(b)

#giáo viên hướng dẫn không ở chung phòng với đồ án mình hướng dẫn
for k in range(K):
    for i in range(N):
        b = model.NewBoolVar('b')
        supervised_teacher = T[i]
        model.Add(x[i][k] == 1).OnlyEnforceIf(b)
        model.Add(x[i][k] != 1).OnlyEnforceIf(b.Not())
        model.Add(y[supervised_teacher-1][k] == 0).OnlyEnforceIf(b)


#hàm mục tiêu cần phải tối đa 

        






solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
    for i in range(N):
        for j in range(K):
            if solver.BooleanValue(x[i][j]):
                X[i] = j+1
    for i in range(M):
        for j in range(K):
            if solver.BooleanValue(y[i][j]):
                Y[i] = j+1
else:
    print('No solution')

#in kết quả
def PRINT(n,m,l1,l2):
    print(n)
    for i in l1:
        print(i,end = ' ')
    print()
    print(m)
    for i in l2:
        print(i,end = ' ')


PRINT(N,M,X,Y)
