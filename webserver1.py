#!/usr/bin/python2
# since in *nix executability is not indicated by file suffixes

# (Can then) start exec with "./webserver1.py"

# Origin: https://ruslanspivak.com/lsbaws-part1/

import socket

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
# Limit the input queue to 1

print 'Serving HTTP on port %s ...' % PORT

# LOOP FOREVER
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    # Receive REQ from browser
    print request

    http_response = """
HTTP/1.1 200 OK

Hello, Adrian!
"""
    # Python uses triple double-quotes to represent multiline strings.
    # HTTP OK type 200 means the REQ was "successful" (in the simplest way)
    # The other part(s) of the response is displayed in the browser pane.
    # A blank is required to separate the 

    client_connection.sendall(http_response)
    client_connection.close()

# Test with http://localhost:8888 in browser.