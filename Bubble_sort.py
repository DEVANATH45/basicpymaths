def Bubble(list):
    swap = True
    while swap:
        swap = False
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                swap = True
    print(list)
n = int(input("Enter the number elements of Array:"))
list = []
for j in range(n):
    list.append(input())
Bubble(list)