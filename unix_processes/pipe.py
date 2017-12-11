#パイプを用いたプロセス間通信
import os
import time

reader, writer = os.pipe()  #ファイルディスクリプタ
pid = os.fork()

if pid:
    # Parent process
    write_pipe = os.fdopen(writer, 'w')
    write_pipe.write('Hello')
    write_pipe.close()
else:
    # Child process
    read_pipe = os.fdopen(reader, 'r')
    content = read_pipe.read(5)
    read_pipe.close()
    print(content)
