

class BaseRequestHandler:
	def __init__(self, server, request, client_address):
		self.server = server
		self.request = request
		self.client_address = client_address

	def handle(self):
		pass


class StreamRequestHandler(BaseRequestHandler):
		def __init__(self, server, request, client_address):
			BaseRequestHandler.__init__(self, server, request, client_address)
			self.rfile = self.request.makefile('rb')
			self.wfile = self.request.makefile('wb')
			self.wbuf = []

		# 编解码：字符串 -> 字节码
		def encode(self, msg):
			if not isinstance(msg, bytes)
				msg = bytes(msg, encoding='utf-8')
			return msg

		# 解码: 字节码 -> 字符串
		def decode(self, msg):
			if isinstance(msg, bytes):
				msg = msg.decode()
			return msg
		
		# 读消息
		def read(self, length):
			msg = self.rfile.read(length)
			return self.decode(msg)

		#  读取一行消息
		def readline(self, length=65536):
			msg = self.rfile.readline(length)
			return self.decode(msg)

		# 写消息
		def write_content(self):
			msg = self.encode(msg)
			self.wbuf.append(msg)
		

		# 发送消息
		def send(self):
			for line in self.wbuf:
				self.wfile.write(line)
			self.wfile.flush()
			self.wbuf = []

		# 
		def close(self):
			self.wfile.close()
			self.rfile.close()
		
