import math
global s
s ='абвгдеёжзиклмнопрстуфхцчшщыъьэюя0123456789.,:;!?abcfvyuiopqwerzm'
kol = len(s)
l = math.ceil(math.log(kol)/math.log(2))
def repl(file1, file2):
	str1 = file1.read()
	str1 = str1.lower()
	str2 = file2.read()
	str2 = str2.lower()
	for i in str1:
		if s.find(i) == -1:
		     str1 = str1.replace(i,'')
	for i in str2:
		if s.find(i) == -1:
		     str2 = str2.replace(i,'')
	return str1, str2

def to_value_(a):
    return s[int(a,2)]
def to_str_(a, s):
    kol = len(s)
    l = math.ceil(math.log(kol)/math.log(2))
    pos = bin(s.find(a))
    pos = pos[2:]
    res = ''
    for i in range(l):
       if pos!='':
          res += pos[0]
          pos = pos[1:]
       else:
          res = '0' + res
    return res
def xor(a,b):
    return (a+b)%2
  

def xor_str(a,b):
    res = ''
    for i in range(len(a)):
        res += str (xor(int(a[i]),int(b[i])))
    return res
def str_to_bin(str1, s):
    res = ''
    for i in str1:
        res += to_str_(i, s)
    return res
def kod(file1, file2, file_out):
	str1, str2 = repl(file1, file2)
	bin_kl = (str_to_bin(str1, s))
	print(bin_kl)
	bin_mes = (str_to_bin(str2, s))
	print(bin_mes)
	if len(bin_kl)<len(bin_mes):
		 kol = len(bin_kl) - 1
		 start = 0
		 while len(bin_kl)<len(bin_mes):
		     val = xor_str(bin_kl[start],bin_kl[start+kol])
		     start += 1
		     bin_kl += val

	print(bin_kl)
	res = xor_str(bin_kl, bin_mes)
	itog = ''
	for i in range(len(str2)):
		itog += to_value_(res[:l])
		res = res[l:]
	print(itog)
	file_out.write(itog)
	file_out.close()
if int(input('0-kod, 1 - dekod')) == 0:
	file1 = open('code.txt', 'r')    
	file2 = open('message.txt', 'r')
	file3 = open('itog.txt', 'w')
	kod(file1, file2, file3)  
else:
	file1 = open('code.txt', 'r')    
	file3 = open('message.txt', 'w')
	file2 = open('itog.txt', 'r')
	kod(file1, file2, file3)  
      

    



