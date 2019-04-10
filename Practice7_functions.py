# 1.Write a function that takes a number and returns the sum of its digits. Raise exception if argument of the wrong type was passed

def sum_digit(num):
    temp=num
    digit=0
    sum=0
    try:
        num=num+0
    except TypeError:
        print("Error Type Error. can only input type \"int\"")
    else:
        while(temp):
            sum +=temp % 10
            temp //= 10
        return sum

def sum_allnum(*input):
    sum=0
    for temp in input:
        if isinstance(temp, int): #可以判断是否继承父类
            sum += temp
    return sum

def length_define(*input):
    input= list(input)
    length=input[0]
    input.pop(0)
    for ele in input:
        if len(ele) <= length:
            input.remove(ele)
    return input

def groupby(f,*str):
    str_dict={}
    for word in str:
        ini_word=f(word)
        print(ini_word)
        if ini_word in str_dict:
            str_dict[ini_word].append(word)
        else:
            str_dict[ini_word]=[word]
    return str_dict

if __name__ == '__main__':
    print("____start_____test1：\n")
    print(sum_digit("1"))
    print("____start_____test2：\n")
    print(sum_allnum("a",1,2,3,4,51231,"b"))
    print("____start_____test3：\n")
    print(length_define(3,"aaasa",'aaaaa',"b"))
    print("____start_____test4：\n")
    print(groupby(lambda s: s[0], 'hello', 'hi', 'help', 'bye', 'here','sadas')) #anonymous functions


