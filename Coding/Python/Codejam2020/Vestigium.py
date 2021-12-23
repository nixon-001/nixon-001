import sys, math, cmath, time

start_time = time.time()


# ---- USER DEFINED INPUT FUNCTIONS ---- #
def inp():
    return int(input1())


def inlt():
    return list(map(int, input1().split()))


def insr():
    s = input1()
    return s[:len(s) - 1]


def invr():
    return map(int, input1().split())


# ---- THE ACTUAL CODE STARTS BELOW ---- #

def solve():
    n = inp()
    a = []
    for i in range(n):
        s = inlt()
        a.append(s)
    q = [[0] * n for i in range(n)]
    w = [[0] * n for i in range(n)]
    qq = 0
    ww = 0
    qw = 0
    for i in range(n):
        for j in range(n):
            q[i][a[i][j] - 1] = q[i][a[i][j] - 1] + 1
        if 0 in q[i]:
            qq = qq + 1
    for i in range(n):
        for j in range(n):
            w[i][a[j][i] - 1] = w[i][a[j][i] - 1] + 1
        if 0 in w[i]:
            ww = ww + 1
    for i in range(n):
        qw = qw + a[i][i]
    print("Case #" + str(tt + 1) + ":", qw, qq, ww)


# ---- THE ACTUAL CODE ENDS ABOVE ---- #
ONLINE_JUDGE = __debug__
if not ONLINE_JUDGE:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
else:
    input1 = sys.stdin.readline
t = 1
t = inp()
for tt in range(t):
    solve()
if not ONLINE_JUDGE:
    print("Time Elapsed:", time.time() - start_time, "seconds")
sys.stdout.close()
