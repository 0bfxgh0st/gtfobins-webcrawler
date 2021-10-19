#!/usr/bin/python3

#######################################
# GTFOBINS.GITHUB.IO WEB SCRAPPER POC #
# by 0bfxGH0ST                        #
#######################################

from bs4 import BeautifulSoup
import requests
import time


print(r"""
._____  _____._._______._______  ._______ .___ .______  .________                                    
:_ ___\ \__ _:|:_ ____/: .___  \ : __   / : __|:      \ |    ___/                                    
|   |___  |  :||   _/  | :   |  ||  |>  \ | : ||       ||___    \                                    
|   /  |  |   ||   |   |     :  ||  |>   \|   ||   |   ||       /                                    
|. __  |  |   ||_. |    \_. ___/ |_______/|   ||___|   ||__:___/                                     
 :/ |. |  |___|  :/       :/              |___|    |___|   :                                         
 :   :/          :        :                                                                          
     :                                                                                               
                                                                                                     
         ___ ._______._______ .________._______ .______  .______  ._______ ._______ ._______.______  
.___    |   |: .____/: __   / |    ___/:_.  ___\: __   \ :      \ : ____  |: ____  |: .____/: __   \ 
:   | /\|   || : _/\ |  |>  \ |___    \|  : |/\ |  \____||   .   ||    :  ||    :  || : _/\ |  \____|
|   |/  :   ||   /  \|  |>   \|       /|    /  \|   :  \ |   :   ||   |___||   |___||   /  \|   :  \ 
|   /       ||_.: __/|_______/|__:___/ |. _____/|   |___\|___|   ||___|    |___|    |_.: __/|   |___\
|______/|___|   :/               :      :/      |___|        |___|                     :/   |___|    
        :                               :                                                            
        :                                                                                            
                                                                                                     

""")

print ("GTFOBins is a curated list of Unix binaries that can be used to bypass local security restrictions in misconfigured systems. The project collects legitimate functions of Unix binaries that can be abused to get the f**k break out restricted shells, escalate or maintain elevated privileges, transfer files, spawn bind and reverse shells, and facilitate the other post-exploitation tasks.")

def Get_Programs():

	url = 'https://gtfobins.github.io'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	programs = soup.find_all('a', class_='bin-name')

	print ("\nGetting gtfobins.github.io database...\n")
	time.sleep(1)
	for i in programs:
		print ( "[+] " + i.text)

def Get_Program_Info():

	select_program = input("\nSelect program: ")

	url = 'https://gtfobins.github.io/gtfobins/' + select_program
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	all = soup.find_all('body')

	print ("Requesting " + select_program + " codes")
	for i in all:
		print (i.text)


Get_Programs()
Get_Program_Info()
