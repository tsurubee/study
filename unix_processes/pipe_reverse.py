#パイプを用いたプロセス間通信
#子→親の通信
import os

reader, writer = os.pipe()

if os.fork():
    # Parent process
    read_pipe = os.fdopen(reader, 'r')
    message = read_pipe.readline()
    read_pipe.close()
    print(message)
else:
    # Child process
    os.close(reader)
    write_pipe = os.fdopen(writer, 'w')
    write_pipe.write('Hello parent!')
    write_pipe.close()
