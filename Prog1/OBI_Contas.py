V = int(input())
A = int(input())
F = int(input())
P = int(input())
c = 0
if V >= A:
    c += 1
    V -= A
if V >= F:
    c += 1
    V -= F
if V >= P:
    c += 1
print(c)