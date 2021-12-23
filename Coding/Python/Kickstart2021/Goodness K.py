s = str(input('enter a string : '))
k = int(input('enter the required goodness : '))
l = len(s)
count = 0
case = 1
if l % 2 == 0:
    for i in range(int(l / 2)):
        if s[i] != s[-i - 1]:
            count += 1
            case += 1
    # print(f"the goodness of {s} is {count}")

else:
    for i in range(int((l - 1) / 2)):
        if s[i] != s[-i - 1]:
            count += 1
            case += 1
    # print(f"the goodness of {s} is {count}")
# print(f'the minimum number of operation to achieve a goodness of {k} is {abs(k - count)}')
print(f'Case #{case}: {abs(k - count)}')
