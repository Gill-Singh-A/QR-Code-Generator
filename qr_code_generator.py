#!/usr/bin/env python3

import qrcode
from datetime import date
from optparse import OptionParser
from time import strftime, localtime
from colorama import Fore, Back, Style

status_color = {
	'+': Fore.GREEN,
	'-': Fore.RED,
	'*': Fore.YELLOW,
	':': Fore.CYAN,
	' ': Fore.WHITE,
}

def get_time():
	return strftime("%H:%M:%S", localtime())
def display(status, data):
	print(f"{status_color[status]}[{status}] {Fore.BLUE}[{date.today()} {get_time()}] {status_color[status]}{Style.BRIGHT}{data}{Fore.RESET}{Style.RESET_ALL}")

def get_arguments(*args):
	parser = OptionParser()
	for arg in args:
		parser.add_option(arg[0], arg[1], dest=arg[2], help=arg[3])
	return parser.parse_args()[0]

if __name__ == "__main__":
	data = get_arguments(('-d', "--data", "data", "Data to store in the QR Code"),
		      			 ('-s', "--save", "save", "Name of the Image file to save the Generated QR Code"),
						 ('-l', "--load", "load", "Load data from the given file"))
	if not data.data:
		if not data.load:
			display('-', "Please specify the data or file from which to load the data")
			exit(0)
		else:
			try:
				with open(data.load, 'r') as file:
					data.data = file.read()
			except FileNotFoundError:
				display('-', f"File {Back.MAGENTA}{data.load}{Back.RESET} not found")
			except:
				display('-', f"Error while reading file {Back.MAGENTA}{data.load}{Back.RESET}")
	qr_code_image = qrcode.make(data.data)
	if not data.save:
		data.save = f"{date.today()}_{get_time()}.png"
	qr_code_image.save(data.save)