import socket
import sys
import threading

# Socks -a simple text messaging app to streach out socket programming skills
# added some text
# more text
def clientthread(conn):
    '''handler for new connections'''
    conn.send(b'welcome to the server, type "quit" to quit\n')

    while 1:
        data = conn.recv(1024)
        reply = 'you said...' + data.decode('utf-8')
        print(data)
        if data[0:4] == b'quit':
            break
        conn.sendall(reply.encode('utf-8'))
    conn.sendall('OK See you later :)\n'.encode('utf-8'))
    conn.close()
    
def startsrv(host='', port=8888):
    ''' start a server listing to tcp port <port> on ip addres <host> '''
    try:    # try to create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        print("doh")
        sys.exit()

    print("created socket")

    s.bind((host, port))
    #print("bound to host: %s on port: %d" % (host, port))

    s.listen(10)

    print("lintening")
    while 1:
        conn, add = s.accept() # accept a new connection- blocking call
        print("Connected with  server")
        p = threading.Thread(target=clientthread, args=(conn,)) # create new thread
        p.start()
    s.close()
