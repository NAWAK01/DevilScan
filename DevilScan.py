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

def mainmenu():
	print bcolors.WARNING
	print "               .        .     ________  _______________   ____.___.____    "
	print "              /(        )`    \______ \ \_   _____/\   \ /   /|   |    |   "
	print "              \ \___   / |     |    |  \ |    __)_  \   Y   / |   |    |   "
	print "              /- _  `-/  '     |    `   \|        \  \     /  |   |    |___"
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
	print "                \       /    type 3 to do a ping test"
	print "           ______( (_  / \______       "
	print "         ,'  ,-----'   |        \      "
	print "         `--{__________)        \/     "
	print "                                       "
	print bcolors.ENDC

	choice = input("enter you choice : > ")

	def choice1():
		# Clear the screen
		subprocess.call('clear', shell=True)
		ipcheck = raw_input("Enter your network ip adress > ")
		print "type 1 to display all ports witch are in testing"
		print "type 2 to display only open ports"
		print "type 3 to test only one specific port"
		print "type 4 to test all port between to values"
		print "              "
		choicescan = input("enter your choice > ")
	
		if choicescan == 1:
			print "wait, it will take a moment..."
			for port in xrange(1, 65536):
 				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				result = sock.connect_ex((ipcheck, port))
				if result == 0:
  					print bcolors.OKGREEN + ">>> Port ", port, " is open on network ", ipcheck
				else:
					print bcolors.WARNING + "Port ", port, " is not open"
			choix = raw_input("Press [Q] to quit, [M] to go to previous menu, and [D] to go to main menu > ")
	
			if choix in ("q", "Q"):
				subprocess.Popen("exit", shell=True)
			elif choix in ("m", "M"):
				choice1()
			elif choix in ("d", "D"):
				mainmenu()
			else:
				print "invalid choice, exiting..."
				time.sleep(3)
				subprocess.Popen("exit", shell=True)
	
		if choicescan == 2:
			print "wait, it will take a moment..."
			for port in xrange(1, 65536):
	 			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				result = sock.connect_ex((ipcheck, port))
				if result == 0:
	  				print bcolors.OKGREEN + ">>> Port ", port, " is open on network ", ipcheck
			choix = raw_input("Press [Q] to quit, [M] to go to previous menu, and [D] to go to main menu > ")
	
			if choix in ("q", "Q"):
				subprocess.Popen("exit", shell=True)
			elif choix in ("m", "M"):
				choice1()
			elif choix in ("d", "D"):
				mainmenu()
			else:
				print "invalid choice, exiting..."
				time.sleep(3)
				subprocess.Popen("exit", shell=True)
	
		if choicescan == 3:
			port = input("enter a port to check > ")
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			result = sock.connect_ex((ipcheck, port))
			if result == 0:
	  			print bcolors.OKGREEN + ">>> Port ", port, " is open on network ", ipcheck
			else:
				print bcolors.WARNING + "Port ", port, " is not open"
			choix = raw_input("Press [Q] to quit, [M] to go to previous menu, and [D] to go to main menu > ")
	
			if choix in ("q", "Q"):
				subprocess.Popen("exit", shell=True)
			elif choix in ("m", "M"):
				choice1()
			elif choix in ("d", "D"):
				mainmenu()
			else:
				print "invalid choice, exiting..."
				time.sleep(3)
				subprocess.Popen("exit", shell=True)
	
		if choicescan == 4:
			rangemin = input("enter the minimum port value > ")
			rangemax = input("enter the maximum port value > ")
			for port in xrange(rangemin, rangemax):
	 			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				result = sock.connect_ex((ipcheck, port))
				if result == 0:
	  				print bcolors.OKGREEN + ">>> Port ", port, " is open on network ", ipcheck
				else:
					print bcolors.WARNING + "Port ", port, " is not open"
			choix = raw_input("Press [Q] to quit, [M] to go to previous menu, and [D] to go to main menu > ")
	
			if choix in ("q", "Q"):
				subprocess.Popen("exit", shell=True)
			elif choix in ("m", "M"):
				choice1()
			elif choix in ("d", "D"):
				mainmenu()
			else:
				print "invalid choice, exiting..."
				time.sleep(3)
				subprocess.Popen("exit", shell=True)


	def choice2():
		print "type 1 for display all ip witch are in testing"
		print "type 2 for display only when a host is found"
		choiceip = input("enter your choice > ")

		if choiceip == 1:
			with open(os.devnull, "wb") as limbo:
				inputip = raw_input("enter you network ip like that : '192.168.1.' > ")
				for n in xrange(1, 255):
					ip=inputip + "{0}".format(n)
					result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
					stdout=limbo, stderr=limbo).wait()
					if result:
						print bcolors.OKBLUE +ip + bcolors.WARNING + " inactive"
					else:
						print bcolors.OKGREEN + ip + " active > HOST FOUND"

			choix = raw_input("Press [Q] to quit, [M] to go to previous menu, and [D] to go to main menu > ")
		
			if choix in ("q", "Q"):
				subprocess.Popen("exit", shell=True)
			elif choix in ("m", "M"):
				choice1()
			elif choix in ("d", "D"):
				mainmenu()
			else:
				print "invalid choice, exiting..."
				time.sleep(3)
				subprocess.Popen("exit", shell=True)
		if choiceip == 2:
			with open(os.devnull, "wb") as limbo:
				inputip = raw_input("enter you network ip like that : '192.168.1.' > ")			
				for n in xrange(1, 255):
					ip=inputip + "{0}".format(n)
					result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
					stdout=limbo, stderr=limbo).wait()
					if result:
						time.sleep(0)
					else:
						print bcolors.OKGREEN + ip + " active > HOST FOUND"
	
			choix = raw_input("Press [Q] to quit, [M] to go to previous menu, and [D] to go to main menu > ")
		
			if choix in ("q", "Q"):
				subprocess.Popen("exit", shell=True)
			elif choix in ("m", "M"):
				choice1()
			elif choix in ("d", "D"):
				mainmenu()
			else:
				print "invalid choice, exiting..."
				time.sleep(3)
				subprocess.Popen("exit", shell=True)
	
	def choice3():
		ipping = raw_input("Enter an ip to test > ")
		requests = raw_input("Enter a number of ping request > ")
		subprocess.Popen(["ping", "-c", requests, "-n", "-W", "2", ipping])
	
		choix = raw_input("Press [Q] to quit, [M] to go to previous menu, and [D] to go to main menu > ")
		
		if choix in ("q", "Q"):
			subprocess.Popen("exit", shell=True)
		elif choix in ("m", "M"):
			choice1()
		elif choix in ("d", "D"):
			mainmenu()
		else:
			print "invalid choice, exiting..."
			time.sleep(3)
			subprocess.Popen("exit", shell=True)	
	
	
	if choice == 1:
		choice1()
	
	if choice == 2:
		choice2()

	if choice == 3:
		choice3()

mainmenu()








