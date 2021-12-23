def checkAttack(qr,qc,opr,opc):
    if qr==opr:
        return True
    elif qc==opc:
        return True
    elif abs(qc-opc)==abs(qr-opr):
        return True
    else:
        return False
n=int(input("enter no of queens:"));lis=[]
for i in range(n):
    t=tuple(map(int,(input().split())))
    lis.append(t)
print(lis)
for i in range(len(lis)):
    for j in range(i+1,len(lis)-1):
        if checkAttack(lis[i][0],lis[i][1],lis[j][0],lis[j][1]):
            print("ATTACK ON TITAN")
    else:
        print("NO ATTACK ON TITAN")




import sys
N = int (input ())
List = []
for i in range (N):
    x = list (map (int, input ().split ()))
    List.append (x)
def check (i, j):
    if i == N:
        print ("NO ATTACK.")
    elif j == N:
        check (i + 1, i + 2)
    else:
        x1, y1 = List[i][0], List[i][1]
        x2, y2 = List[j][0], List[j][1]
        if ((x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2) or (x1 == x2) or (y1 == y2)):
            print ("ATTACK.")
            sys.exit ()
        check (i, j + 1)
check (0, 1)

