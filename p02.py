#!/usr/bin python
# coding=utf-8
import os
import sys
import string
import json
import re



sys.path.append(os.getcwd())



# http://www.pythonchallenge.com/pc/def/map.html

def solve(s0):
    s1 = ''
    for ch in s0:
        if ch >= 'a' and ch <= 'x':
            ch = chr(ord(ch) + 2)
        elif ch == 'y':
            ch = 'a'
        elif ch == 'z':
            ch = 'b' 
        s1 += ch
    print(s1)

s0 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
solve(s0)

s1 = "map"
solve(s1)
# ocr

intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = str.maketrans(intab, outtab)


print(s0.translate(trantab))

print(s1.translate(trantab))



