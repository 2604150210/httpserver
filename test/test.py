
from server.socket_server import TCPServer
from handler.base_handler import StreamRequestHandler

class TestBaseRequestHandler(StreamRequestHandler):
    # 具体的处理逻辑

    def handle(self):
        pass


# 测试SocketServer(TCPServer)
class SocketServerTest:

    def run_server(self):
        tcp_server = TCPServer('127.0.0.1', 8888, TestBaseRequestHandler)
        tcp_server.server_forever()

    # 客户端的具体链接逻辑
    def client_connet(self):
        client = socket.socket()
        client.connect(('127.0.0.1', 8888))

    def gen_clients(self, num):
        clients = []
        for i in range(num):
            client_thread = threading.Thread(target=self.client_connet)
            clients.append(client_thread)
        return clients

    def run(self):
        server_thread = threading.Thread(target=self.run_server)
        server_thread.start()

        clients = self.gen_clients(10)
        for client in clients:
            client.start()

        server_thread.join()
        for client in clients:
            client.join()

if __name__ == '__main__':
    SocketServerTest().run()








