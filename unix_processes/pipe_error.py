#パイプを用いたプロセス間通信
#双方向の通信ができないことの確認
import os

reader, writer = os.pipe()

if os.fork():
    # Parent process
    os.close(reader)
    write_pipe = os.fdopen(writer, 'w')
    write_pipe.write('Hello child!')
    write_pipe.close()
else:
    # Child process
    os.close(writer)
    read_pipe = os.fdopen(reader, 'r')
    message = read_pipe.readline()
    read_pipe.write('Hello parent!')  #readerから書き込んでみる
    read_pipe.close()
    print(message)

#エラー結果
#Traceback (most recent call last):
#  File "pipe_error.py", line 18, in <module>
#    read_pipe.write('Hello parent!')
#io.UnsupportedOperation: not writable
