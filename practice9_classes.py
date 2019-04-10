class Widget(object):
    dependency_obj=[]
    dependency=[]
    name=[]
    def __init__(self, name):
        self.name = name

    def add_dependency(self,*args):
        for i in args:
            self.dependency_obj.append(i)

    def build(self):
        self.recur_dependency(self)
        print(self.dependency)

    def recur_dependency(self,obj):
        for i in self.dependency_obj:   #Recursively search for dependency
            if i.dependency_obj:
                if i.name not in obj.dependency:
                    obj.dependency.append(i.name)
            else:
                i.recur_dependency(obj)

luke    = Widget("Luke")
hansolo = Widget("Han Solo")
leia    = Widget("Leia")
yoda    = Widget("Yoda")
padme   = Widget("Padme Amidala")
anakin  = Widget("Anakin Skywalker")
obi     = Widget("Obi-Wan")
darth   = Widget("Darth Vader")
_all    = Widget("All")


luke.add_dependency(hansolo, leia, yoda)
leia.add_dependency(padme, anakin)
obi.add_dependency(yoda)
darth.add_dependency(anakin)

print(luke.dependency_obj)
luke.build()
_all.add_dependency(luke, hansolo, leia, yoda, padme, anakin, obi, darth)
_all.build()


class MusicFile():
    artis_dic = {}
    arti_class_dic = {}
    def __init__(self, link):
        self.link = link
        with open(link, 'r') as f:
            txt = f.read()
        txt=txt.split('\n')
        for i in txt:
            line=i.split('-',1)
            line[0]=line[0].strip(' ')
            if line[0] not in self.artis_dic:
                self.artis_dic[line[0]]=[]
                self.artis_dic[line[0]].append(line[1])
            else:
                self.artis_dic[line[0]].append(line[1])
        for i in self.artis_dic:
            if i not in self.arti_class_dic:
                self.arti_class_dic[i]=self.creat_artist(i,self.artis_dic[i])

    def creat_artist(self,name,song):
        return self.artist_ini(name,song)

    def artist(self,art_name):
        return self.arti_class_dic[art_name]

    class artist_ini():
        def __init__(self,name,song):
                self.artist_name=name
                self.songs=song

music = MusicFile('./practice9.txt')
print(music.artist('Joy Division').songs)
