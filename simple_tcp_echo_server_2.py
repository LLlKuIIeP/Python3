import threading
import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(('0.0.0.0', 2222)) 
s.listen(10)

def fun():
        while True:
                conn, addr = s.accept()
                while True:
                        data = conn.recv(1024)
                        if data == 'close':
                                break
                        conn.send(data)
                conn.close()


for i in xrange(10):
        t = threading.Thread(target=fun)
        t.start()
