#fork(2)システムコールによりプロセスが生成されることを確認する
#if句が親プロセスによって実行され、else句が子プロセスによって実行されていることがわかる。

import os

print("parent process pid: {0}".format(os.getpid()))

if os.fork():
    print("Here in the if block. pid: {0}".format(os.getpid()))
else:
    print("Here in the else block. pid: {0}".format(os.getpid()))
