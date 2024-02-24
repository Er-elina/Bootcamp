def fib(n):
    n1,n2=0,1
    count=0
    while (n==1):
        print(n)
        print(n1)

def fib1(n):
    n1,n2=0,1
    count=0
    while count<n:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1
