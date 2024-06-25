import socket

'''
    sanity check works if the connection to port 80 works
    and the connection on port 81 fails
'''

# connect to web server on port 80
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(3)
res = sock.connect_ex(('100.100.6.2', 80))
if res == 0:
    print('[+] Successfuly connected to webserver on port 80')
# connect to web server on port 81
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(3)
res = sock.connect_ex(('100.100.6.2', 81))
if res != 0:
    print('[+] Not connected to webserver on port 81')


# connect to google
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(3)
res = sock.connect_ex(('216.58.214.164', 80))
if res == 0:
    print('[+] Successfuly connected to google on port 80 with ipv4')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(3)
res = sock.connect_ex(('216.58.214.164', 4567))
if res != 0:
    print('[+] Not connected to google on port 4567 with ipv4')

# connect to google
sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
sock.settimeout(3)
res = sock.connect_ex(('2a00:1450:4007:80c::2004', 80))
if res == 0:
    print('[+] Successfuly connected to google on port 80 with ipv6')

sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
sock.settimeout(3)
res = sock.connect_ex(('2a00:1450:4007:80c::2004', 4567))
if res != 0:
    print('[+] Not connected to google on port 4567 with ipv6')
