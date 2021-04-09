def factorial():

 def fact(n):
    fac=1
    for i in range(1,n+1):

        fac=fac*i
    return fac
 n=int(input("Enter the number:"))
 if n<0:
    print("Enter a postive number!!")

 elif n==0:
    print("Factorial of the given number is:0")
 else:
    print("Factorial of the given number is :"+str(fact(n)))
