# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 23:37:11 2020

@author: HP
"""

def copyfile(oldfile,newfile):
    f1=open(oldfile,"r")
    f2=open(newfile,"w")
    while true:
        text=f1.read(5)
        if text=="":
            break
        f2.write(text)
        f1.close()
        f2.close()