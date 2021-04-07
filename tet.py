#-*-coding:utf8;-*-
#qpy:console
import socket
import sys

print ("   ______  _____   _____   _____  ")
print ("  |___  / | ____| /  ___| /  ___/ ")
print ("     / /  | |__   | |     | |___  ")
print ("    / /   |  __|  | |  _  \___  \ ")
print ("   / /__  | |___  | |_| |  ___| | ")
print ("  /_____| |_____| \_____/ /_____/ ")


print("let's do that")
hostname = input()
ip=socket.gethostbyname(hostname)
print('Host Name Is:' ,hostname, '\n''target Ip Is: ',ip)