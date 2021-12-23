a = int(input())
for b in range(a):
    l = int(input())
    li = list(map(int , input().split()))
    tot = 0
    for i in range(len(li)-1):
        k = li[i]
        j = li.index(min(li[i:]))
        li[i:j+1] = reversed(li[i:j+1])
        tot = tot + j - i +1
        # print(k, j, tot, li)
    print(f'Case #{b + 1}: {tot}')
