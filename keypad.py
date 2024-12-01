s=""
for x in input():
    tn = ord(x) - 97
    n = tn // 3 + 2
    if x in "pqrs":
        n = 7
        nt = "pqrs".index(x) + 1
    elif x in "tuv":
        n = 8
        nt = "tuv".index(x) + 1
    elif x in "wxyz":
        n = 9
        nt = "wxyz".index(x)+1   
    else:
        nt = tn % 3 + 1
    s += str(n) * nt
print(s)
