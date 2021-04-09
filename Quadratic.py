import cmath
def Quadratic_function():
 def input_1():
    print("Enter the elements a,b,c of the quadratic equation:\n")
    a=int(input())
    b=int(input())
    c=int(input())
    r=[a,b,c]
    return r
 def quad(x,y,z):
    s=(y*y)-(4*x*z)
    q=cmath.sqrt(s)
    r1=(-y+q)/(2*x)
    r2=(-y-q)/(2*x)
    return[r1,r2,s]


 r=input_1()
 x=r[0]
 y=r[1]
 z=r[2]

 p=quad(x,y,z)

 print("The equation is :{0}x^2+{1}x+{2}".format(x,y,z))

 if p[2]==0:
    print("Roots are equal\n.")
 elif p[2]<0:
    print("Roots are complex.\n")
 else:
    print("Roots are natural.\n")

 print("Solution to the given equation is:{0},{1}".format(p[0],p[1]))
Quadratic_function()







