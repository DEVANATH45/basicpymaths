# lex_auth_01269438594930278448

def find_pairs_of_numbers(num_list, n):
    count = 0
    sum = 0
    for i in range(len(num_list)):
        for j in range((i + 1), (len(num_list))):
            sum = num_list[i] + num_list[j]
            if sum == n:
                count += 1
    for k in num_list:
        if k == n:
            count += 1
        elif k==0:
            count -=1

    return count


num_list = [1,2,7,4,5,6,0,3]
n = 6
print(find_pairs_of_numbers(num_list, n))