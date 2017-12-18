#パイプを用いたプロセス間通信
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
    read_pipe.close()
    print(message)
