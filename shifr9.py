file = open('code.txt', 'r')
str = file.read()
str = str.lower()
b = ''
dict = {}
matr = []
matr1 = []
for i in range(97,123):
    b += (chr(i))
a = b.replace('j','')
print("alphabet")
print(a)

ii=0
jj=0
kol = len(str)
for i in range (kol):
  if ii> 4:
      matr.append(matr1)
      matr1 = []
      ii = 0
      jj+=1
  if a.find(str[i])!=-1:
      matr1.append(str[i])
      dict[str[i]] = ii * 10 + jj
      a = a.replace(str[i],'')
      ii+=1
kol = len(a)

for i in range (kol):
  if ii> 4:
      matr.append(matr1)
      matr1 = []
      ii = 0
      jj+=1
  matr1.append(a[0])
  dict[a[0]] = ii * 10+ jj
  a = a.replace(a[0],'')
  ii+=1

matr.append(matr1)
file1 = open('message.txt', 'r')
print(matr)
STROKA = file1.read()
STROKA = STROKA.lower()
STROKA = STROKA.replace('j','i')
i = 0
num = 0

while i <len(STROKA):
  if b.find(STROKA[i])== -1:
    STROKA = STROKA.replace(STROKA[i],'')
  else:
      i+=1

i = 0
newstr = ''
while i <len(STROKA):
  zn1 = STROKA[i]
  zn2 = STROKA[i+1]
  zn11 = zn1 / 10
  zn12 = zn1 % 10
  zn21 = zn2 / 10
  zn22 = zn2 % 10
  if zn11 == zn21:
      if zn12 == 4: zn12 = -1
      if zn22 == 4: zn22 = -1
      newstr += matr[zn11][zn12 + 1]
      newstr += matr[zn21][zn22 + 1]
  elif zn12 == zn22:
      if zn11 == 4: zn11 = -1
      if zn21 == 4: zn21 = -1
      newstr += matr[zn11+1][zn12]
      newstr += matr[zn21+1][zn22]
  else:
      newstr += matr[zn11][zn22]
      newstr += matr[zn21][zn12]
  i+=2

    
file2 = open('itog.txt', 'w')
file2.write(newstr)
file2.close()
    
      
  
