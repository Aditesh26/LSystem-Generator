import socket

SERVER = "irc.libera.chat"
PORT = 6667
NICK = "Aditesh_test"
channel = "#test"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER, PORT))

print("Server Connected")

data = sock.recv(4096)
print(data.decode("utf-8", "ignore"))

def send(cmd):
    msg = cmd + "\r\n"
    sock.sendall(msg.encode("utf-8"))
    print(">>"+cmd)


send("NICK "+NICK)
send(f"USER {NICK} 0 * :{NICK}")



while True:
    data = sock.recv(4096)
    data = data.decode("utf-8", "ignore")
    if data.startswith("PING"):
        response = data.replace("PING","PONG")
        send(response.strip())

