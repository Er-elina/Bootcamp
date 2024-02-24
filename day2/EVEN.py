def even(n):
   # for num1 in range(100):
        if(n%2==0):
            return "it is even"
        else:
            return "it is not even"
def evenrange(start,end):
    result=[]
    for n in range(start,end+1):
        if(n%2==0):
            result.append(n)
            return result