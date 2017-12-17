#fork後のプロセスIDがどうなっているか調べる
#if句が親プロセス、else句が子プロセスによって実行されていることがわかる。
import os

print("---- before fork ----")
print("pid: {0}".format(os.getpid()))

if os.fork():
    print("----- if block ------")
    print("pid: {0}".format(os.getpid()))
else:
    print("---- else block -----")
    print("pid: {0}".format(os.getpid()))
