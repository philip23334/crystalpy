#!/usr/bin/env python3

# --------------------------------------------------------------
#         CrystalPy - A lightweight Python http server
# --------------------------------------------------------------
#TODO Add More Functionality

#! BECAUSE THIS ONLY SUPPORTS ONE FILE DOESN'T MEAN ITS A BUG, ITS A FEATURE :D

import os
if os.name == 'posix':os.system('clear')
else:os.system('cls')

# Import The Needed stuff
from server_settings import *

import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = 'src/'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
    def do_POST(self):
        self.path = 'src/'
        return http.server.SimpleHTTPRequestHandler.do_POST(self)

# Create an object of the above class
handler_object = MyHttpRequestHandler

server = socketserver.TCPServer((HOST, PORT), handler_object)

# Star the server
print("[" + PREFIX + "] Server started at address http://"+ HOST + ":" + str(PORT))
print("[" + PREFIX + "] Hello from the CrystalPy Community, FYI CrystalPy is a lightweight Python http server, it is limited to a single file, that is index.html! You cannot use external files like .css files or .js files, sorry, will work on it for later.")
print("[" + PREFIX + "] You can use this server for testing purposes, but it is not recommended for production use.")
print("[" + PREFIX + "] You can also use javascript files from other servers, png files from other servers, css files from other servers, etc.")
print("[" + PREFIX + "] Made with <3 by the CrystalPy Community")
server.serve_forever()