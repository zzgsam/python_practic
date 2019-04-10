import sys
import csv

def read_file(file_path):
    file_to_read= open(file_path, "r")  # 读成char的list
    txt=file_to_read.read()
    #txt = txt.lower()
    file_to_read.close()
    return txt

def symbol_replace(txt):
    txt=txt.replace('=',' ')
    return txt

def txt_processing(txt):
    csv_list=[]
    csv_list.append(['interface','inet','status'])#list的第一个元素为各个元素的分类
    interface=[]
    txt=txt.replace('status:','status')#处理读取string中的status:
    str=txt.split()#变成word的list
    interface_num = 0
    inet = ''
    status = ''

    for i,word in enumerate(str):
        if word == 'flags':#检测到flags就把interface给存储起来
            interface_num +=1
            str[i-1]=str[i - 1].replace(':', '')#去除interface中的:
            interface.append(str[i-1])
            print(str[i-1])
            if interface_num > 1:
                csv_list.append([interface[interface_num-2],inet,status])#添加新的list的element
            inet = ''
            status = ''
        if word == 'inet':
            inet=str[i+1]
        if word == 'status':
            status = str[i+1]
    csv_list.append([interface[interface_num-1],inet,status])
    return csv_list

def write_to_csv(csv_list):
    print(csv_list)
    file_name='practice3.csv'
    with open(file_name,'w',newline='') as f: #如果不指定newline='',则每写入一行将有一空行被写入。上面的代码生成如下内容。用于替代直接的open。
        writer=csv.writer(f)
        for row in csv_list:#一个list的元素写一行
            writer.writerow(row)

if __name__ == '__main__':
    print("start\n")
    file_path=sys.argv[1]
    txt = read_file(file_path)
    txt = symbol_replace(txt)
    csv_list=txt_processing(txt)
    print(csv_list) #[['interface', 'inet', 'status'], ['lo0', '127.0.0.1', ''], ['gif0', '', ''], ['en0', '10.176.85.19', 'active'], ['en1', '', 'inactive'], ['p2p0', '', 'inactive']]
    write_to_csv(csv_list)
