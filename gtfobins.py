#!/usr/bin/python3

#######################################
# GTFOBINS.GITHUB.IO WEB SCRAPPER POC #
# by 0bfxGH0ST                        #
#######################################

from bs4 import BeautifulSoup
import requests
import sys
import os

def _header_():
	print ('\033[1;31m')
	print (r"""
._____  _____._._______._______  ._______ .___ .______  .________                                    
:_ ___\ \__ _:|:_ ____/: .___  \ : __   / : __|:      \ |    ___/                                    
|   |___  |  :||   _/  | :   |  ||  |>  \ | : ||       ||___    \                                    
|   /  |  |   ||   |   |     :  ||  |>   \|   ||   |   ||       /                                    
|. __  |  |   ||_. |    \_. ___/ |_______/|   ||___|   ||__:___/                                     
 :/ |. |  |___|  :/       :/              |___|    |___|   :                                         
 :   :/          :        :                                                                          
     :                                                                                               """)
	print ('\033[0m')
	print ("\033[1;31mGTF0Bins \033[0m\033[32mis a curated list of Unix binaries that can be used\nto bypass local security restrictions in misconfigured systems.\nThe project collects legitimate functions of Unix binaries that\ncan be abused to get the f**k break out restricted shells, escalate or maintain\nelevated privileges, transfer files, spawn bind and reverse shells\nand facilitate the other post-exploitation tasks.\033[0m\n")

def _request_gtfobins_frontend_db_():

	url = 'https://gtfobins.github.io'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	programs = soup.find_all('a', class_='bin-name')

	for i in programs:
		print ( "[\033[32m+\033[0m] " + i.text)

def _request_program_info_():

	select_program = input("\n[(\033[33mGTF0BINS\033[0m)]> ")

	url = 'https://gtfobins.github.io/gtfobins/' + select_program
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	print ("\n[\033[1;33m" + select_program.upper() + "\033[0m]")

	for i in soup.find_all(["ul","h2","p"]):

		print(i.text.replace('Sudo','\033[1;32m[Sudo]\033[0m').replace('SUID','\033[1;32m[SUID]\033[0m').replace('File read','\033[1;32m[File read]\033[0m').replace('File write','\033[1;32m[File write]\033[0m').replace('Shell','\033[1;32m[Shell]\033[0m').replace('Reverse shell','\033[1;32m[Reverse shell]\033[0m').replace('File upload','\033[1;32m[File upload]\033[0m').replace('File download','\033[1;32m[File download]\033[0m').replace('Library load','\033[1;32m[Library load]\033[0m').replace('Capabilities','\033[1;32m[Capabilities]\033[0m').replace('Limited \033[1;32m[SUID]\033[0m','\033[1;32m[Limited SUID]\033[0m').replace('Non-interactive reverse shell','\033[1;32m[Non-interactive reverse shell]\033[0m').replace('Non-interactive bind shell','\033[1;32m[Non-interactive bind shell]\033[0m').replace('Command','\033[1;32m[Command]\033[0m'))

def _argv_():

	url = 'https://gtfobins.github.io/gtfobins/' + sys.argv[1]
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	print ("\n[\033[1;33m" + sys.argv[1].upper() + "\033[0m]")

	for i in soup.find_all(["ul","h2","p"]):
		print(i.text.replace('Sudo','\033[1;32m[Sudo]\033[0m').replace('SUID','\033[1;32m[SUID]\033[0m').replace('File read','\033[1;32m[File read]\033[0m').replace('File write','\033[1;32m[File write]\033[0m').replace('Shell','\033[1;32m[Shell]\033[0m').replace('Reverse shell','\033[1;32m[Reverse shell]\033[0m').replace('File upload','\033[1;32m[File upload]\033[0m').replace('File download','\033[1;32m[File download]\033[0m').replace('Library load','\033[1;32m[Library load]\033[0m').replace('Capabilities','\033[1;32m[Capabilities]\033[0m').replace('Limited \033[1;32m[SUID]\033[0m','\033[1;32m[Limited SUID]\033[0m').replace('Non-interactive reverse shell','\033[1;32m[Non-interactive reverse shell]\033[0m').replace('Non-interactive bind shell','\033[1;32m[Non-interactive bind shell]\033[0m').replace('Command','\033[1;32m[Command]\033[0m'))


if len(sys.argv) == 2:

	_header_()
	_argv_()

else:

	try:
		_header_()
		_request_gtfobins_frontend_db_()
		_request_program_info_()

	except KeyboardInterrupt:

		print ("\n\n[\033[31m-\033[0m] Killing gtfobins.py\n")
		sys.exit(1)
