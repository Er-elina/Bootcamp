def checkprime(num):
    for i in range(2,num):
        if(num%i == 0):
            return False
            break
            
        else:
            return True
def primerange(start,end):
    primenumbers=[]
    for number in range(start,end):
        if(checkprime(num1)==True):
            primenumbers.append(num1)
    return primenumbers
            