# This is easyNetScanner v1 - the simple network scanner. Created by Dmitry https://github.com/gtashnik
# needs Python v3 to be installed


import os
import socket
import sys

def menuRunner():
	print('1 - The subnet scanner')
	print('2 - The port scanner')
	print('0 - Exit')

	print('-----------------------')

	menu = int(input ('Enter menu number to run the program: ' ))



	if menu == 1:
		subnetscan()
	
	elif menu == 2:
		portscan()
		
	
	elif menu == 0:
		print('Good bye')
		exit()
	
	else:
		print('You enterred wrong menu number. PLease,execute this soft again') 
		
	

def subnetscan():
	subnet = input('Enter subnet, for example 255.255.255. : ')

	prt = input('Enter port to be ckecked for available, for example: 80:  ') #address of port to be checked

	ipList = [] ; i = 0

	while i <= 255:
		ipList.append(str(subnet) + str(i))
		i = i + 1
	
	ipOutput = [] #creating an output

	for ipItem in ipList:
		ipsock = socket.socket()
		ipsock.settimeout(1)
	
		try:
			ipsock.connect((ipItem, int(prt)))	
		except socket.error:
			pass
		else:
			ipsock.close
		
			
			print(ipItem + ': ' + ' host is active on port ' + str(prt)) #printing the list of scanned items to console
			ipOutput.append(ipItem + ': ' + ' host is active on port ' + str(prt)) #adding data to ouptut
		
	print ("--------------------------------")
	print ("Subnet scanning finished")
	print('-----------------------')
	print('#')
	
	f = open( (subnet + '_' + str(prt) + '_ip_result.txt'), 'w', encoding='utf-8'	) # creatig a file to write

	for item in ipOutput:
		f.write('%s\n' % item)
	f.close() #closing file
	
	menuRunner() # here execute menuRunner
		
	# END OF SUBNETSCAN FUNCTION

def portscan():
	host = input('Enter domain name or IP address: ')
	portBegin = input('Enter first number of port you want to scan (from 0 to 65 535: ')
	portEnd = input('Enter last number of port you want to scan (from ' + str(portBegin) + ' to 65 535: ')

	portList = range(int(portBegin), int(portEnd))


# print(portList)

	portOutput = [] #creating an output

	for port in portList:
		sock = socket.socket()
		sock.settimeout(1)
		try:
			sock.connect((host, port))
		except socket.error:
			pass
		else:
			sock.close
			print (host + ': ' + str(port) + ' port is active')
			portOutput.append(host + ': ' + str(port) + ' port is active') #adding data to ouptut
	print ("--------------------------------")
	print ("Port scanning finalized")
	print('-----------------------')
	print('#')
	
	f = open( (host + '_ip_ports_result.txt'), 'w', encoding='utf-8'	) # creatig a file to write

	for item in portOutput:
		f.write('%s\n' % item)
	f.close() #closing file
	
	menuRunner()
		
	# END OF PORTSCAN FUNCTION
	

menuRunner() #executing menu 



