from termcolor import colored
def read_txtLines(file):
	try:
		with open(file,'r') as textfile:
			lines = textfile.readlines()
			return lines
	except Exception as e:
		print(colored(e,'red')) 
		raise SystemExit