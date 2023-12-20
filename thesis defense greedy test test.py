N,M,K = map(int,input().split())
a,b,c,d,e,f = map(int,input().split())
C = []
G = []
for _ in range(N):
    rowC = list(map(int,input().split()))
    C.append(rowC)


X = [0 for i in range(N)]
Y = [0 for i in range(M)]

def Sum_X(x,k_thesis,room):
    sum = 0
    return sum

def check(x,index,k):
    check_variable = True
    if x.count(k) >= b:
        check_variable = False
    for i in range(index):
        if x[i] == k and C[i][k] < e:
            check_variable = False
    return check_variable


#xét k trường hợp của X có thể từ X1 -> Xk trong đó Xi[0] = i
allX = []
for i in range(K):
    X[0] = i + 1
    allX.append(list(X))  # create a new list for each entry in allX

for Xi in allX:
    SumXi = 0
    for nth_thesis in range(1, N):
        for room in range(1, K + 1):
            if check(Xi, nth_thesis, room):
                
                    Xi[nth_thesis] = room
          
    print(Xi)
