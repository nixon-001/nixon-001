# l1 = [1,2,3,4]
# l2 = ['hi', 'hello', 'bye!!']
# l3 = [True, False]
# print(*l1, sep = '\n')

# li = [1,2, [3,4]]
# li[2].insert(2,5)
# li.extend([6,7,8])
# print(li)


# li = [1,2,3,[4,5,6,7]]
# li1 = []
# for i in li:
#     li1.append(i)
# for i in li:
#     if type(i) != list:
#         pass
#     elif len(i)>1:
#         print(i)

# t=["a","b","c"]
# y=["c","d"]
# y.append(t)
# print(y)
# l=len(y)
# t1=len(t)
# for j in range(t1):
#     print(y[2][j])'


s1=input()
s2=input()

l1,l2,l3,l4=[],[],[],[]
l1=s1.split()
l2=s2.split()
# print(s1,s2)
for i in range(len(l1)):
    if l1.count(l1[i])>1:
        l1.remove(i,l1[i])
        
for j in range(len(l2)):
    if l2.count(l2[i])>1:
        l2.remove(j,l2[j])

for i in l1:
    s1=i
    
for j in l2:
    s2=j

r1 = []
r2 = []

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            l3=s1.split(s1[i])
            l4=s2.split(s2[j])
            r1.append(l3[0]+s1[i]+l4[1])
            r2.append(l4[0]+s1[i]+l3[1])
            
        l3=[]
        l4=[]
r1.sort()
r2.sort()

for i in r1:
    print(i)
for i in r2:
    print(i)


s1 = str(input())
s2 = str(input())
l1 = list(s1)
l2 = list(s2)
l3 = []
l4 = []

for i in l1:
    if i not in l3:
        l3.append(i)
        
for i in l2:
    if i not in l4:
        l4.append(i)
        
l5 = []
l6 = []
l7 = []
l8 = []
        
for i in l3:
    if i in l4:
        l5.append(l3[:l3.index(i)+1])
        l6.append(l4[l4.index(i)+1:])
        l7.append(l4[:l4.index(i)+1])
        l8.append(l3[l3.index(i)+1:])
        
for i in l5:
    n = l5.index(i)
    for i in l6[n]:
        l5[n].append(i)
        
for i in l7:
    n = l7.index(i)
    for i in l8[n]:
        l7[n].append(i)

r1 = []
r2 = []

for i in l5:
    x = ''.join(i)
    r1.append(x)
    
for i in l7:
    x = ''.join(i)
    r2.append(x)

r1.sort()
r2.sort()

for i in r1:
    print(i)
for i in r2:
    print(1)
