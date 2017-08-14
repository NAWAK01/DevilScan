import time
import socket
import os
import re
import subprocess
import sys
from datetime import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print bcolors.WARNING
print "               .        .     ________  _______________   ____.___.____    "
print "              /(        )`    \______ \ \_   _____/\   \ /   /|   |    |   "
print "              \ \___   / |     |    |  \ |    __)_  \   Y   / |   |    |   "
print "              /- _  `-/  '     |    `   \|        \  \     /  |   |    |_  "
print "             (/\/ \ \   /\    /_______  /_______  /   \___/   |___|_______ \ "
print "             / /   | `    \           \/        \/                        \/ "
print "             O O   ) /    |      _________ _________     _____    _______    "
print "             `-^--'`<     '     /   _____/ \_   ___ \   /  _  \   \      \   "
print "            (_.)  _  )   /      \_____  \  /    \  \/  /  /_\  \  /   |   \  "
print "             `.___/`    /       /        \ \     \____/    |    \/    |    \ "
print "               `-----' /       /_______  /  \______  /\____|__  /\____|__  / "
print "  <----.     __ / __   \               \/          \/         \/         \/   "
print "  <----|====O)))==) \) /====           "
print "  <----'    `--' `.__,' \    type 1 for open port testing"
print "               |        |    type 2 for scann all ip connected to your network"
print "                \       /    type 3 to do a ping test (close terminal to stop)"
print "           ______( (_  / \______       "
print "         ,'  ,-----'   |        \      "
print "         `--{__________)        \/     "
print "                                       "
print bcolors.ENDC

time.sleep(3)
choice = input("enter you choice : > ")

if choice == 1:
	# Clear the screen
	subprocess.call('clear', shell=True)
	ipcheck = raw_input("Enter your network ip adress > ")
	port = input("Enter the port > ")
 	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex((ipcheck, port))
	if result == 0:
  		print bcolors.OKGREEN + "Port ", port, " is open"
		print bcolors.WARNING + "scan finished. exit."
		time.sleep(2)
		exit()
	else:
		print bcolors.WARNING + "Port ", port, " is not open"
		print bcolors.WARNING + "scan finished. exit."
		time.sleep(2)
		exit()
if choice == 2:
	print " ip scanner "
	with open(os.devnull, "wb") as limbo:
		for n in xrange(1, 255):
			ip="192.168.1.{0}".format(n)
			result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
			stdout=limbo, stderr=limbo).wait()
			if result:
				print bcolors.OKBLUE +ip + bcolors.WARNING + " inactive"
			else:
				print bcolors.OKGREEN + ip + " active > HOST FOUND"
if choice == 3:
	ipping = raw_input("Enter an ip to test > ")
	subprocess.Popen(["ping", ipping])
