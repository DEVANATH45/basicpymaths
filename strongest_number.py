def factorial(number):
    if number==0:
        return 1
    fac=1
    for i in range(1,number+1):
        fac=fac*i
    return fac


def find_strong_numbers(num_list):
    l=[]
    for i in num_list:
        su=0
        temp =i
        while(i>0):
            d = i % 10
            i = i // 10
            su += factorial(d)
        if temp==su:
            l.append(temp)
    return l

num_list=[145,375,100,2,10,0,40585]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)