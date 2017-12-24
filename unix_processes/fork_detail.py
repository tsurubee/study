import os

print("---- before fork ----")
print("pid: {0}".format(os.getpid()))
ret = os.fork()

if ret:
    print("----- if block ------")
    print("pid: {0}".format(os.getpid()))
    print("return value: {0}".format(ret))
else:
    print("---- else block -----")
    print("pid: {0}".format(os.getpid()))
    print("return value: {0}".format(ret))
