import socket
import threading

SERVER = "irc.libera.chat"
PORT = 6667
NICK = "Aditesh_test"
channel = "#test"



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER, PORT))

print("Server Connected")

data = sock.recv(4096)
print(data.decode("utf-8", "ignore"))

state = {
    "nick": NICK,
    "connected": True,
    "channel": None
}


def send(cmd):
    msg = cmd + "\r\n"
    sock.sendall(msg.encode("utf-8"))
    print(">>"+cmd)

send("NICK "+NICK)
send(f"USER {NICK} 0 * :{NICK}")


def user_input():
    while True:
        msg = input()
        if msg.startswith("/quit"):
            send("QUIT :client exiting")
            state["connected"] = False
            sock.close()
            break
        elif msg.startswith("/join"):
            parts = msg.split()
            if len(parts) == 2:
                channel = parts[1].strip()
                send(f"JOIN {channel}")
                state["channel"] = channel

            else:
                print("Usage: /join <channel>")

        else:
            if state["channel"]:
                send(f"PRIVMSG {state['channel']} :{msg}")
            else:
                print("You are not connected to a channel")





threading.Thread(target=user_input, daemon=True).start()
reg = False
while state["connected"]:
    try:
        data = sock.recv(4096)
    except (ConnectionAbortedError, OSError):
        print("Connection closed")
        break
    data = data.decode("utf-8", "ignore")
    if not data:
        state["connected"] = False
        sock.close()
        break
    print(data)

    if data.startswith("PING"):
        response = data.replace("PING","PONG")
        send(response.strip())

    if " 001 " in data and not reg:
        print("Registered with server")
        reg = True

    if "PRIVMSG" in data:
        prefix, message = data.split("PRIVMSG", 1)

        sender = prefix.split("!")[0][1:]
        target, text = message.split(" :", 1)

        print(f"<{sender}> {text.strip()}")
