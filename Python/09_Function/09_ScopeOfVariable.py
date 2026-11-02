n = 1   # Global Variable

def fun():
    # Local Variable
    global n
    n = 5
    print('in',n)

fun()
print('out',n)
