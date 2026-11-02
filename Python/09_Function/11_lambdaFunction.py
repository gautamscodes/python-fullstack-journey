# Lambda Function and Anonymous function

def add(a):
    return a + 1

res = add(2)
print(res)

# lambda
fun = lambda a : a + 1
res2 = fun(5)
print(res2)

fun2 = lambda a, b: a + b
res3 = fun2(30,40)
print(res3)
