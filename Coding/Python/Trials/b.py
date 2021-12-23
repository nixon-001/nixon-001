from math import ceil
n = int(input())
l = []
for i in range(n**2):
    l.append(input())
def swap(li,pos1, pos2):
    li[pos1], li[pos2] = li[pos2], li[pos1]
    return li
l1 = l[:n-1]

for i in range(n**2):
    if (i+1)%n==0:
        l1.append(l[i])
l1+=l[n**2-n+1:n**2-1][::-1]
for i in range(n**2-1,0,-1):
    if i%n==0 and i!=0:
        l1.append(l[i])
l2=[]
print(l1)
print(l1[len(l1)-len(l1)%3-1])
for i in l:
    if i not in l1:
        l2.append(i)
# x,y = 0,2
# for i in range(ceil(len(l1)/3)+1):
#     l1 = swap(l1,x,y)
#     x+=2
#     y+=2
x,y = 0,2
print(l1[11])
while l[0]!=l1[len(l1)-len(l1)%3-1]:
    print(l1[len(l1)-len(l1)%3-1],x,y)
    l1 = swap(l1,x,y)
    x+=2
    y+=2

print(l1)
print(l2)


