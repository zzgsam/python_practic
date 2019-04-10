#Write a program that asks the user for a number(Interger) and prints the sum of its digits

def ask_user():
    num = input("Input a number")
    print(type(num),num)    #type() returns the type of a variable
                            #isinstance(a, int) returns true or false
    sum=0
    for num_add in num:
        sum += int(num_add)
    print("sum = %d" % sum)
    pass
ask_user()
