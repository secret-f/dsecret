# the main file of this project

import bhash as bh
import random, fao, time
from hashlib import sha384
from static import *

# version number

VERSION_NUMBER = "1030"

# some easy functions

def _sec(p):
    r = bh.bhash(hash(p)%256)
    return _lower_16xletter_list[(r&0xf0)//16]+_lower_16xletter_list[r&15]

def _sha(b):
    return sha384(b).hexdigest()

def _random():
    s0, s1, s2, s3, s4 = [random.choice(_upper_16xletter_list) for i in '     ']
    return b''.join((s0, s1, s2, s3, s4))

# encrypt and decrypt with a 32kb limit

def _encode(content, password):
    assert len(content)<=32768
    result = b''
    c = _sec(password)
    for i in _range_32k:
        if len(content)==i: break
        n = _dict_all_16x[_all_bytes[c[0]]]*16+_dict_all_16x[_all_bytes[c[1]]]
        result += _all_bytes[(ord(_all_bytes[content[i]])-n)%256]
    return result

def _decode(content, password):
    assert len(content)<=32768
    result = b''
    c = _sec(password)
    for i in _range_32k:
        if len(content)==i: break
        n = _dict_all_16x[_all_bytes[c[0]]]*16+_dict_all_16x[_all_bytes[c[1]]]
        result += _all_bytes[(ord(_all_bytes[content[i]])+n)%256]
    return result

# encrypt and decrypt files

def encode(ff, tf, pf, FAO=False, log=False):
    ff = open(ff, 'rb')
    tf = open(tf, 'wb')
    pf = open(pf, 'wb')
    pf.write(b"DSECRET")
    while True:
        content = ff.read(32768)
        if not content: break
        pwd = _random()
        pf.write(b'-')
        pf.write(pwd)
        spwd = bytes(_sha(pwd), 'ascii')
        n = _encode(content, spwd)
        if FAO:
            n = fao.fao_e(n)
        tf.write(n)
        if log: print("32KB wrote in")
    ff.close()
    tf.close()
    pf.close()
    return 1

def decode(ff, tf, pf, FAO=False, log=False):
    pf = open(pf, 'rb')
    pf.read(8)
    pwd = pf.read()
    pf.close()
    pwd = pwd.split(b'-')
    ff = open(ff, 'rb')
    tf = open(tf, 'wb')
    for i in range(len(pwd)):
        content = ff.read(32768)
        n = _decode(content, bytes(_sha(pwd[i]), 'ascii'))
        if FAO:
            n = fao.fao_d(n)
        tf.write(n)
        if log: print("32KB wrote in")
    ff.close()
    tf.close()
    return 1

