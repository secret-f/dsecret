CMD_NOT_FOUND = 4
CMD_ARG_ERROR = 2
CMD_VERIFY_FAIL = 1
CMD_ACCESS = 0

class DymanicArgnum():

    def __init__(self, t):
        self.least = t[0]
        self.most = t[1]
    
    def isable(self, n):
        return self.least<=n and n<=self.most

class Cmd():

    def __init__(self, prompt, commands, argnum, verify=None):
        self.cmd = commands
        self.prompt = prompt
        self.argnum = argnum
        if verify is not None:
            self.verify = True
            self.verify_func = verify[0]
            self.verify_list = verify[1]
        else:
            self.verify = False
    
    def run(self):
        incmd = input(self.prompt)
        args = incmd.split()
        if not incmd.strip():
            return
        if self.cmd.get((func:=args[0])) is None:
            return CMD_NOT_FOUND
        if len(args)-1!=self.argnum[func]:
                if not self.argnum[func].isable(len(args)-1):
                    return CMD_ARG_ERROR
        if self.verify:
            if func in self.verify_list and not self.verify_func():
                return CMD_VERIFY_FAIL
        self.cmd[func](*(args[1:]))
        return CMD_ACCESS
