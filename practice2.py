#take a file name as command line argument, count how many times each word appears in the file and prints the world
#that appears the most
#如果想对python脚本传参数，python中对应的argc, argv(c语言的命令行参数)是什么呢？
# 需要模块：sys
# 参数个数：len(sys.argv)
import sys

def read_file(file_path):
    file_to_read= open(file_path, "r")  # 读成char的list
    txt=file_to_read.read()
    txt = txt.lower()
    file_to_read.close()
    return txt

def replace(txt):
    for ch in ',~!@#$%^&*()_+"{}[]|?.<>?\n':
        txt = txt.replace(ch,' ')  # ch被替换成空.注意: 如果ch替换成''会导致s\n1\n.....替换成s11111.注意在赋值为''空时候，相当于list这个值被去掉了
    return txt

def word_dict(txt):
    word_dic = {}
    str = txt.split()  # 通过空格或者\n进行分割成词
    # print(str)
    for word in str:  # 判断词语是否已经在字典中出现
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    print(word_dic)
    return word_dic


'''
print("name of the script: %s" % sys.argv[0])  #python practice2.py a bsda jkas: length l=4
print(len(sys.argv))
for i in range(1,len(sys.argv)):
    print(i)

# fileHandle = open("test.txt",w)
# fileHandle.write ( '\n\nBottom line.' )   #write

txt=open("./temp/t1.txt","r").read() #读成char的list
txt=txt.lower()

for ch in ',~!@#$%^&*()_+"{}[]|?.<>?\n':
    txt=txt.replace(ch,'') #ch被替换成空

word_dic={}
str=txt.split() #通过空格或者\n进行分割成词
for word in str:    #判断词语是否已经在字典中出现
    if word in word_dic:
        word_dic[word] += 1
    else:
        word_dic[word]=1
word_lis=word_dic.items() #将dic变成list
word_lis=sorted(word_lis,key=lambda x:x[1],reverse=True) #比较list中每两个的数字排序。逆序排列。也可以按key排列 key=lambda d:d[0]
print(word_lis[0][0])
'''

if __name__ == '__main__':
    print('start \n')
    file_path= sys.argv[1]
    print(file_path)
    txt=read_file(file_path)
    txt=replace(txt)
    print(txt)
    dic=word_dict(txt)
    word_lis = dic.items()  # 将dic变成list
    word_lis = sorted(word_lis, key=lambda x: x[1], reverse=True)  # 比较list中每两个的数字排序。逆序排列。也可以按key排列 key=lambda d:d[0]
    print("%s appears %d times" % (word_lis[0][0],word_lis[0][1])) #注意print%后为一个list，要用()包含打印内容


