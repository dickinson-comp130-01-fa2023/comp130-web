def add5(x):
    y = x + 5
    print(x, 'plus 5 is', y)
    mult_by3(y)


def mult_by3(m):
    n = 3 * m
    print(m, 'times 3 is', n)
    sub7(n)

def sub7(w):
    v = w - 7
    print(w, 'minus 7 is', v)


z = 10
add5(z)
