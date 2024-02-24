def oddrange(start,end):
    result=[]
    for num in range(start,end+1):
        if(num%2!=0):
            result.append(num)
        return result
def odd(num1):
    if(num1%2==0):
        return "it is not odd"
    else:
        return"it is odd"