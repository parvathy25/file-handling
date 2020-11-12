# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 01:54:16 2020

@author: HP
"""

>>> import pickle
>>> f =open("C:\\Users\\Parvathy\\Documents\\file1.txt","w")
>>> n = [8,3,9,1,3]
>>> s = pickle.dumps(n)
>>> f.close()
>>> f =open("C:\\Users\\Parvathy\\Documents\\file1.txt","r")
>>> t = pickle.loads(s)
>>> t.sort()
>>> cp =[]
>>> for a in t:
... if a not in cp:
... cp.append(a)
... print(cp)
[1, 3, 8, 9]
>>> str = ",".join(str(i) for i in cp)
>>> f.close()
>>> f =open("C:\\Users\\Parvathy\\Documents\\file1.txt","w")
>>> f.write(str)
7
>>> f.close()
>>> def copyFile(oldFile, newFile):
... f1 = open(oldFile, "r")
... f2 = open(newFile, "w")
... while True:
... text = f1.read(50)
... if text == "":
... break
... f2.write(text)
... f1.close()
... f2.close()
... return
...
>>>
copyFile("C:\\Users\\Parvathy\\Documents\\file1.txt","C:\\Users\\Parvathy\\Documents\\file2.txt
")
>>> newfile = open("C:\\Users\\Parvathy\\Documents\\file2.txt","r")
>>> print(newfile.read())
1,3,8,9