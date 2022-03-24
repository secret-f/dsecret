import cmdapi, dsecret, sys, random

help_doc = '''\
help - 显示帮助

write <未加密文件> <目标文件> <密码存储文件> - 为文件加密
read <加密文件> <目标文件> <密码存储文件> - 为文件解密
quit - 退出\
'''

def help():
    print(help_doc)

def verify():
    num = random.randint(100000, 999999)
    print("验证码是：%d"%num)
    return input("请输入验证码：")==str(num)


cmds = {
    "read": dsecret.decode, 
    "write": dsecret.encode, 
    "help": help, 
    "quit": sys.exit
}
argnum = {
    "read": 3, 
    "write": 3, 
    "help": 0, 
    "quit": 0
}
verify_list = ["read"]

cmd = cmdapi.Cmd('> ', cmds, argnum, (verify, verify_list))
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
