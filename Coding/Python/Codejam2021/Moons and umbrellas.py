k = int(input())
for i in range(k):
    X, Y, S = input().split()
    def main():
        x = int(X)
        y = int(Y)
        s = str(S)
        s = s.upper()
        s = s.replace('?', '')
        cj = (s.count('CJ')) * x
        jc = (s.count('JC')) * y
        r = cj + jc
        print(f'Case #{i + 1}: {r}')
    main()

