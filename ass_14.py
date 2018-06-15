#1
import subprocess
def tail(f, n, offset=0):
    proc = subprocess.Popen(['tail', '-n', n + offset, f], stdout=subprocess.PIPE)
    lines = proc.stdout.readlines()
    return lines[:, -offset]

#2
file=open("C:\\Users\\Akshay","r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k,v in wordcount.items():
    print (k, v)



#3
import os
import shutil
import tempfile

filename1 = tempfile.mktemp (".txt")
open (filename1, "w").close ()
filename2 = filename1 + ".copy"
print (filename1, "=>", filename2)
shutil.copy (filename1, filename2)
if os.path.isfile (filename2): print ("Success")
dirname1 = tempfile.mktemp (".dir")
os.mkdir (dirname1)
dirname2 = dirname1 + ".copy"
print (dirname1, "=>", dirname2)
shutil.copytree (dirname1, dirname2)
if os.path.isdir (dirname2): print ("Success")

#4
with open('abc.txt') as fh1, open('test.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
        print(line1+line2)

#5
import random
def Rand(start, end, num):
    res = []
    for j in range(num):
        res.append(random.randint(start, end))
    return res
num = 10
start = 20
end = 40
print(Rand(start, end, num))