import dsecret, sys, random, os
from cmdapi import *

help_doc = '''\
help - 显示帮助

encrypt <未加密文件> <目标文件> <密码存储文件> - 为文件加密
decrypt <加密文件> <目标文件> <密码存储文件> - 为文件解密
quit - 退出\
'''

inf = float('inf')


def help():
    print(help_doc)

def run_system_cmd(*args):
    return os.system(' '.join(args))


cmds = {
    "decrypt": dsecret.decode, 
    "encrypt": dsecret.encode, 
    "run": run_system_cmd, 
    "help": help, 
    "quit": sys.exit
}
argnum = {
    "decrypt": DymanicArgnum((3, 4)), 
    "encrypt": DymanicArgnum((3, 4)), 
    "run": DymanicArgnum((1, inf)), 
    "help": 0, 
    "quit": DymanicArgnum((0, 1))
}

cmd = Cmd('> ', cmds, argnum)
print("Document secret文件加密程序 版本", dsecret.VERSION_NUMBER)
try:
    while True:
        res = cmd.run()
        if res:
            if res&1:
                print("验证失败。")
            if res&2:
                print("参数错误。使用 help 查看帮助。")
            if res&4:
                print("错误的命令。使用 help 查看帮助。")
except KeyboardInterrupt: 
    pass
