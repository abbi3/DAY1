#file
'''f = open("prolog.txt","r")
print(f.readline())'''

'''f = open("prolog.txt","r")
for x in f:
    print(f)'''

'''f = open("prolog.txt","a")
f.write("there is one more line in the file now")'''

'''f = open("abc.txt","a")
f.write("mihir")'''

'''import os
os.remove("abc.txt")'''

'''import os
if os.path.exists("prolog.txt"):
    os.remove("prolog.txt")
else:
    print("file does not exists")'''
'''import os
f = open("demo.txt","a")
f.write("mihir")
print(f.name)
print(f.close())
print(f.mode)
f.close()'''

'''import os
f = open("demo.txt","r+")
f1 = f.read(10)
print(f1)
h1=f.read()
print(h1)'''

'''f = open("demo.txt","r+")
str  = f.read(10)
print("read a string",str)
position = f.tell()
print("current position of the file pointer",position)
position = f.seek(0,10)
str = f.read(10)
print("again the file to be read is",str)
f.close()'''

