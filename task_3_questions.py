# Question 1
def hello_name(user_name):
    print("hello_" + user_name +"!")


# Question 2
odd_numbers = []
n = 1
while len(odd_numbers) < 100:
    if n % 2 == 1:
        odd_numbers.append(n)
    n += 1

for odd_number in odd_numbers:
    print(odd_number)


# Question 3
def max_num_in_list(a_list):
    return(max(a_list))


# Question 4
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        elif a_year % 100 != 0:
            return True
    else:
        return False

# Question 5
def is_consecutive(a_list):
    for i in range(len(a_list)):
        if i == 0:
            i += 1
            continue

        if a_list[i] - 1 != a_list[(i-1)]:
            return False
            break
        
    return True