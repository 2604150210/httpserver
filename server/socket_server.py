
import socket

class TCPServer:
    def __init__(self, server_address, handler_class):
        self.server_address = server_address
        self.HandlerClass = handler_class
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.is_shutdown = false
    # 服务器的启动函数
    def server_forerver(self):
        self.socket.bind(self.server_address)
        self.socket.listen(10)
        # while True:
        while not self.is_shutdown:
            # 1. 接受请求
            request, client_address = self.get_request()
            # 2. 处理请求
            try:
                self.process_request(self, request, client_address)
            except Exception as e:
                print(e)
            finally:
                # 3. 关闭连接
                self.close_request(request)
        pass

    # 接受请求
    def get_request(self):
        return self.socket.accepted()

    # 处理请求
    def process_request(self, request, client_address):
        handler = self.HandlerClass(request, client_address)
        handler.handle()
        pass

    # 关闭请求
    def close_request(self, request):
        request.shutdown(socket.SHUT_WR)
        request.close()
        pass

    # 关闭服务器
    def shutdown(self):
        self.is_shutdown = True
        pass