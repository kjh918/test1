a = 0
b = 1
n = 3
while n < 11:
    p = a + b
    print(p)
    a = b
    b = p
    n += 1

def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def mer(lis_1: list,lis_2: list,n: int) -> int:
    result = [] 
    if n == 1:
        return lis_2
    else:
        for i in lis_1:
            for j in lis_2:
                result.append(i+j)
        return mer(lis_1,result,n-1)

print(mer(['A','T','G','C'],['A','T','G','C'],3))
print(mer(['A','T','G','C'],['A','T','G','C'],2))
print(mer(['A','T','G','C'],['A','T','G','C'],1))




            
