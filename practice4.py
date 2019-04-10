import sys

def read_file(file_path):
    file_to_read= open(file_path, "r")  # 读成char的list
    txt=file_to_read.read()
    file_to_read.close()
    return txt

def txt_processing(txt):
    str = ''
    name=''
    track=''
    year=''
    mus_format=''
    minus_num=0
    output=[]
    for ch in txt:
        if ch == '-' and minus_num == 0:
            minus_num +=1
            str=str.strip()
            album=str
            name = str
            str = ''
        elif ch == '(':
            str=str.strip()
            track = str
            str = ''
        elif ch == ')':
            str=str.strip()
            year = str
            str = ''
        elif ch == '\n':
            str=str.strip()
            mus_format = str
            str = ''
            output.append(name+'/'+year+' '+name+'/'+track+mus_format)
            name=track=year=mus_format=''
            minus_num=0
        else:
            str +=ch
    return output

if __name__ == '__main__':
    print("start\n")
    file_path=sys.argv[1]
    txt=read_file(sys.argv[1])
    expect_output=txt_processing(txt)
    print(expect_output)
