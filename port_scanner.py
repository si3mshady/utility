import socket 

global server_ip 

server_ip = '127.0.0.1'

def a_scanner_darkly(port):
    soc = socket.socket()
    try:
        soc.connect((server_ip)) #testing port connectivity 
        return True 
    except: 
        return False 
    finally: 
        soc.close()

def begin():
    for port in list(range(0,1024)):
        if a_scanner_darkly(port):
            print("CONNECTED to port {}".format(port))
        else:
            print("Unable to connnect to port {}".format(port))

if __name__ == "__main__":
    begin()

    #port scanner 