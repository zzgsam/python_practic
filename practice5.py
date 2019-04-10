import os

if __name__== '__main__':
    file_name=os.listdir('./practice5')
    print(file_name)
    c_str = []
    py_str = []
    pl_str = []
    for str in file_name:
        file_name = 'practice5.txt'
        if ".h" in str or ".c" in str:
            print(str)
            c_str.append(str)

        if ".py" in str or ".pyc" in str:
            print(str)
            py_str.append(str)
        if ".pl" in str or ".pm" in str:
            print(str)
            pl_str.append(str)
    print(c_str)
    c_str.append('\n')
    py_str.append('\n')
    pl_str.append('\n')
    with open(file_name, 'a+') as f:  # 如果不指定newline='',则每写入一行将有一空行被写入。上面的代码生成如下内容。用于替代直接的open。
        f.write('c and h file:'+"\n")
        f.writelines(c_str)
        f.write('py and pyc file:\n')
        f.writelines(py_str)
        f.write('pl and pm file:\n')
        f.writelines(pl_str)