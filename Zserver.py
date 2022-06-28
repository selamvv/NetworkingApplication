#!/usr/bin/python3
import sys
from socket import *


class Connection()

    def serverConnection():
        serverPort = 8080
        #create socket for client with network type and tcp socket specification
        serverSocket= socket(AF_INET, SOCK_STREAM)
        #establish server port
        serverSocket.bind(('', serverPort))
        #wait for client 
        serverSocket.listen(1)
        print('Ready to recieve')
        #create a unique connection to every new client...eventually store in dict
        while True:
            connectionSocket, addr = serverSocket.accept()
            sentence = connectionSocket.recv(1024).decode()
            #do something
            #close connection for just specific client
            connectionSocket.close()
            
        
def main():
    
main()

