
def ams():
 n=int(input("Enter the number tp check:"))
 temp=n
 times=0
 sum=0
 while temp>0:
    times=times+1
    temp//=10
 temp=n
 while temp>0:
    r=temp%10
    sum=sum+(r**times)
    temp//=10
 if sum==n:
    print("The number is an amstrong number")
 else:
    print("The number is not an amstrong number")
