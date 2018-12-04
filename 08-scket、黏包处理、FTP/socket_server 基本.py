import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print("err：",e)
                break
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    # Create the server, binding to localhost on port 9999
    #每来一个新的请求，就会新增一个线程来进行处理，支持同时处理多个请求
    # server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler) #ThreadingTCPServer多并发服务器
    server =socketserver.TCPServer((HOST, PORT), MyTCPHandler)  #只支持单线程请求处理
    server.serve_forever()
