file = open('code.txt', 'r')
str2 = file.read()
str2 = str2.lower()
str2 = 'winter, земляника, земляника.'


# Прочитаем набор байтиков из файла на диске
#data = file.read()


# Запишем байты обратно на диск
#file1.write(data)

#file1.close()  # Необязательно, но хороший стиль


class Foo(object):
    def __init__(self, name):
       self.name = name
  
    def __str__(self):
       return '%s' % self.name

a = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя!.,?-:;"()0123456789'
b = Foo(a)
strr= ''
for i in range(len(str2)):
    if a.find(str2[i])!= -1 and strr.find(str2[i])==-1:
        strr += str(Foo(str2[i]))
for i in range(len(a)):
    if strr.find(a[i])== -1:
        strr += str(Foo(a[i]))
        
#strr = str(b)
print(strr)
a = strr
def kod(file,file1):

    for line in file:
        for i in range(len(line)):
            pos = strr.find(line[i])
            if pos>-1:
                file1.write(strr[len(strr) - pos - 1])
                print(strr[len(strr) - pos - 1])
            else:
                file1.write(line[i])
                print(line[i])

                
print('0 - kod, 1 - dekod')
d = int(input())
if d == 0:
    file = open('text1.txt', 'r')
    file1 = open('text.txt', 'w')
    kod(file,file1)
elif d == 1:
    file = open('text.txt', 'r')
    file1 = open('text2.txt', 'w')
    kod(file,file1)
print("finish")
        


