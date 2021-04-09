def check_double(number):
    cnt = 0
    n = 2*number
    l = list(map(int,str(n)))
    lnumber = list(map(int,str(number)))

    if len(l) == len(lnumber):
        for i in range(len(l)):
            t = l[i]
            for j in lnumber:
                if t == j:
                    cnt += 1
                    break
        if cnt == len(l):
            return "True"
        else:
            return "False"
    else:
        return "False"


# Provide different values for number and test your program
print(check_double(141131))