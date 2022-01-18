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
	print (r"""GTFOBins is a curated list of Unix binaries that can be used
to bypass local security restrictions in misconfigured systems.
The project collects legitimate functions of Unix binaries that
can be abused to get the f**k break out restricted shells, escalate or maintain
elevated privileges, transfer files, spawn bind and reverse shells,
and facilitate the other post-exploitation tasks.
""")

def _request_gtfobins_frontend_db_():

	url = 'https://gtfobins.github.io'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	programs = soup.find_all('a', class_='bin-name')

	for i in programs:
		print ( "[\033[32m+\033[0m] " + i.text)

def _request_program_info_():

	print ('\nuse python3 gtfobins.py --download-db to download gtfobins database')
	select_program = input("\n[(\033[33mGTF0BINS\033[0m)]> ")

	url = 'https://gtfobins.github.io/gtfobins/' + select_program
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	print ("\n[\033[1;33m" + select_program.upper() + "\033[0m]")

	for i in soup.find_all(["ul","h2","p"]):
		print(i.text)


def _request_all_and_save_():

        try:
                os.remove('/tmp/gtfobinsdb.txt')
        except OSError:
                pass

        url = 'https://gtfobins.github.io'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        programs = soup.find_all('a', class_='bin-name')

        for i in programs:

                allurl = 'https://gtfobins.github.io/gtfobins/' + i.text
                file = open('/tmp/gtfobinsdb.txt', 'a')
                file.write('\n\n' + allurl + '\n\n' + "[ " + i.text.upper() + " ]\n")
                print ('Downloading ' + allurl)
                page = requests.get(allurl)
                soup = BeautifulSoup(page.content, 'html.parser')
                for j in soup.find_all(["ul","h2","p"]):
                        file.write(j.text + "\n")

        file.close()
        print ('\nFile stored in /tmp/gtfobinsdb.txt')

try:
	if sys.argv[1] == "--download-db":

		_request_all_and_save_()
		sys.exit(1)
except IndexError:
	pass

try:
	_header_()
	_request_gtfobins_frontend_db_()
	_request_program_info_()
except:
	print ("\n\n[\033[31m!\033[0m] Closing gtfobins.py\n")
	sys.exit(1)
