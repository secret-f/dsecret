from static import *

# 通过栈的方式拖延解密时间以增强安全性

def fao_e(b):
    l = list(b)
    s = []
    r = []
    while len(l)>=5:
        for i in _range_5:
            s.append(l.pop())
        for i in _range_4:
            r.append(s.pop())
    while l:
        s.append(l.pop())
    while s:
        r.append(s.pop())
    for i in range(len(r)):
        r[i]=_all_bytes[r[i]]
    return b''.join(r)

def  fao_d(b):
    l = list(b)
    s = []
    r = []
    lenth = len(l)
    last = lenth%5
    times = lenth//5
    for i in range(times+last):
        s.append(l.pop())
    for i in range(last):
        r.append(s.pop())
    for i in range(times):
        for j in _range_4:
            s.append(l.pop())
        for j in _range_5:
            r.append(s.pop())
    for i in range(len(r)):
        r[i]=_all_bytes[r[i]]
    return b''.join(r)