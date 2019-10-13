
import socket
def server():
    # 1. 创建套接字
    s = socket.socket()
    # 2. 绑定
    HOST = '127.0.0.1'
    PORT = 6666
    s.bind((HOST, PORT))
    # 3. 监听
    s.listen(5)
    # 4. 处理
    while True:
        c, addr = s.accept()
        print('Connect client:  ', addr)
        msg = c.recv(1024)
        print('Receive msg: %s' %msg)
        c.send(msg)
    pass

if __name__ == '__main__':
    server()