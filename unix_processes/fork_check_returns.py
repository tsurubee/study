#fork後の返り値がどうなっているか調べる
#親プロセス側には「生成した子プロセスのpid」を返し、
#子プロセス側には「0」を返すことがわかる。
import os

ret = os.fork()

if ret:
    print("----- if block ------")
    print("return value: {0}".format(ret))
else:
    print("---- else block -----")
    print("return value: {0}".format(ret))
