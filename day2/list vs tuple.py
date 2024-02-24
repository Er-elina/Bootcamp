## LIST VS TUPLE
List
* list is mutable
* The list is better for performing operations, such as insertion and deletion.
* Lists consume more memory
* Lists have several built-in methods
* Unexpected changes and errors are more likely to occur
#Tuple
* Tuple is immutable
* A Tuple data type is appropriate for accessing the elements
* Tuple consumes less memory as compared to the list
* Tuple does not have many built-in methods.
* In a tuple, it is hard to take place.

## When to use list and when to use tuple
for example:
    List = [1, 2, 3, 4, 3, 3, 3]
print("Original list ", List)
List[4] = 7
print("show mutability ", List)
# output :
Original list=[1,2,3,4,3,3,3]
show mutability= [1, 2, 3, 4, 7, 3, 3]
"""  list is use any number remove ,add ,extend . list is store in value 2 memory blocks """
 Tuple=(1,2,3,4,5)
 print("result",Tuple[2])
    #output: result 3
    """ tuple is store in value 1 memory block ,they don’t require extra space for new objects"""
    
    ##Difference between parameter and arguments
    #parameter
   *  Parameters are defined by the names that appear in a function definition
   *  Parameters define what kind of arguments a function can accept.
    # Here a,b are the parameters
     def sum(a,b): 
  print(a+b) 
    
sum(1,2)
    
#Argument 
*Arguments are the values actually passed to a function when calling it.
def sum(a,b):
    print(a+b)
 # here 1,2 are the arguments
 sum (1,2)