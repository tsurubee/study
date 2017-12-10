import os
import sys
import time

ret = os.fork()

if not ret:
    time.sleep(5)
    print("Child task is done!")
    sys.exit()

time.sleep(2)
print(os.wait()) #子プロセスの終了を待つ
print("Parent task is done!")
sys.exit()
