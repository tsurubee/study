#親プロセスが子プロセスより先に終了して、孤児プロセスになった場合、
#子プロセスのppidがどうなるか確認する。

import os
import sys
import time

if os.fork():
    print("parent process pid: {0}".format(os.getpid()))
    sys.exit()
else:
    time.sleep(1)
    print("ppid: {0}".format(os.getppid()))
    sys.exit()
