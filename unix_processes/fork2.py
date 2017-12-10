import os

print("parent process pid: {0}".format(os.getpid()))
ret = os.fork()

if ret:
    print("----- if block ------")
    print("pid: {0}".format(os.getpid()))
    print("return value: {0}".format(ret))
    print("---------------------")
else:
    print("---- else block -----")
    print("pid: {0}".format(os.getpid()))
    print("return value: {0}".format(ret))
    print("---------------------")
