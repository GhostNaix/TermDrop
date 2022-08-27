import os
import sys
import platform
import colorama
import tarfile
import base64
import time
import datetime
colorama.init(autoreset=True)
Version = 'v2.2'
CWD = os.getcwd()

def Print_Error(text):
	print (colorama.Fore.RED + '[-] ' + colorama.Fore.CYAN + str(datetime.datetime.now()) + colorama.Style.RESET_ALL + " " + text)
	return;

def Print_Good(text):
	print (colorama.Fore.BLUE + '[+] ' + colorama.Fore.CYAN + str(datetime.datetime.now()) + colorama.Style.RESET_ALL + " " + text)
	return;

def Print_Info(text):
	print (colorama.Fore.WHITE + '[*] ' + colorama.Fore.CYAN + str(datetime.datetime.now()) + colorama.Style.RESET_ALL + " " + text)
	return;

def Print_Alert(text):
	print (colorama.Fore.YELLOW + '[!] ' + colorama.Fore.CYAN + str(datetime.datetime.now()) + colorama.Style.RESET_ALL + " " + text)
	return;

def Print_cyan(text):
	print (colorama.Fore.CYAN + text)
	return;

def Print_Yellow(text):
	print (colorama.Fore.YELLOW + text)
	return;

def Print_Green(text):
	print (colorama.Fore.GREEN + text)
	return;


def help():
	Print_Good("Help command detected ! Printing help menu")
	Print_Info ("""TermDrop syntax:
Usage """ + sys.argv[0] + """ [options]
Options:
  -h, --help                                Displays this help menu

  -c, --compress [Filename or foldername]   Compresses a folder or a file and
                                            encode it in base64.

  -d, --decompress [Filename]               Decode the base64 encoded file/folder 
                                            and decompress it. 

""")
	return;


def decompress(argv, argv_lowercase):
	Print_Good("Decompress argument detected")
	if (len(argv) < 2):
		Print_Error("You have not specified a valid input file or directory")
		Print_Info ('Refer to: "' + colorama.Fore.YELLOW + sys.argv[0] + '" -h' + colorama.Style.RESET_ALL + '" for a list of valid commands')
		sys.exit(1)
	if (len(argv) > 2):
		Print_Error("You have specified too many arguments")
		Print_Info ('Refer to: "' + colorama.Fore.YELLOW + sys.argv[0] + '" -h' + colorama.Style.RESET_ALL + '" for a list of valid commands')
		sys.exit(1)
	if (not os.path.isfile(argv[1])):
		Print_Error("The file you specified does not exists")
		sys.exit(1)
	time.sleep(2)
	Print_Info("Decoding base64 file")
	try:
		b64_file = open (argv[1], 'r')
		b64_content = b64_file.read()
		content = base64.b64decode(b64_content)
		tar_file = open ("Compressed_tool.tar.gz", 'wb')
		tar_file.write(content)
		tar_file.close()
		b64_file.close()
	except Exception as e:
		Print_Error(str(e))
		Print_Error("An error has occurred whilst attempting to decode the file")
		Print_Info("Please ensure that you can read/write in the current directory and the file is encoded in base64")
		sys.exit(1)
	Print_Info("Successfully decoded the file to tar.gz")
	time.sleep(2)
	Print_Info("Decompressing the base64 decoded file \"Compressed_tool.tar.gz\"")
	try:
		tar_file = tarfile.open('Compressed_tool.tar.gz')
		tar_file.extractall(".")
		tar_file.close()
	except Exception as e:
		Print_Error(str(e))
		Print_Error("An error has occurred whilst attempting to write the decoded file")
		Print_Info("Please ensure that you can read/write in the current directory and the file is encoded in base64")
		sys.exit(1)
	time.sleep(2)
	Print_Info("Successfully decompressed the file Compressed_tool.tar.gz")
	Print_Info("Cleaning up")
	try:
		if (os.path.exists ("Compressed_tool.tar.gz")):
			os.remove("Compressed_tool.tar.gz")
		else:
			Print_Alert("I could've sworn this file was present a few seconds ago !")
			Print_Alert("I think somebody or something has moved or deleted the file")
	except Exception as e:
		Print_Error(str(e))
		Print_Alert("An error has occurred whilst attempting to clean up the directory")
		Print_Info("Please ensure that you can write in the current directory")
	Print_Good("Clean up procedure completed")
	time.sleep(2)
	Print_Good("The directory containing the file/directory you requested is named \"Compress_tool\" ")
	sys.exit(0)
	return

def compress(argv, argv_lowercase):
	Print_Good("Compress argument detected")
	if (len(argv) < 2):
		Print_Error("You have not specified a valid input file or directory")
		Print_Info ('Refer to: "' + colorama.Fore.YELLOW + sys.argv[0] + '" -h' + colorama.Style.RESET_ALL + '" for a list of valid commands')
		sys.exit(1)
	if (len(argv) > 2):
		Print_Error("You have specified too many arguments")
		Print_Info ('Refer to: "' + colorama.Fore.YELLOW + sys.argv[0] + '" -h' + colorama.Style.RESET_ALL + '" for a list of valid commands')
		sys.exit(1)
	if (not os.path.exists(argv[1])):
		Print_Error("The file or folder you specified does not exists")
		sys.exit(1)
	time.sleep(2)
	Print_Info("Compressing to tar.gz file format")
	try:
		tar_file = tarfile.open("Compressed_tool.tar.gz", "w:gz")
		tar_file.add(argv[1])
		tar_file.close()
	except Exception as e:
		Print_Error(str(e))
		Print_Error("An error has occurred whilst attempting to compress the file/directory")
		Print_Info("Please ensure that you can write in the current directory")
		sys.exit(2)
	time.sleep(2)
	Print_Good("Successfully compressed the requested file/directory")
	Print_Info("Encoding in base64")
	try:
		tar_file = open ("Compressed_tool.tar.gz", 'rb')
		compress_content = tar_file.read()
		base64_content = base64.b64encode(compress_content).decode('ascii')
		b64_file = open ("Compressed_tool.b64", 'w')
		b64_file.write(base64_content)
		tar_file.close()
		b64_file.close()
	except Exception as e:
		Print_Error(str(e))
		Print_Error("An error has occurred whilst attempting to encode the file/directory")
		Print_Info("Please ensure that you can read and write in the current directory")
		sys.exit(2)
	time.sleep(2)
	Print_Good("Successfully base64 encoded the tar.gz file")
	time.sleep(2)
	Print_Info("Cleaning up")
	try:
		if (os.path.exists ("Compressed_tool.tar.gz")):
			os.remove("Compressed_tool.tar.gz")
		else:
			Print_Alert("I could've sworn this file was present a few seconds ago !")
			Print_Alert("I think somebody or something has moved or deleted the file")
	except Exception as e:
		Print_Error(str(e))
		Print_Alert("An error has occurred whilst attempting to clean up the directory")
		Print_Info("Please ensure that you can write in the current directory")
	Print_Good("Clean up procedure completed")
	time.sleep(2)
	Print_Good("The file containing the file/directory you requested is named \"Compressed_tool.b64\"")
	sys.exit(0)
	return

def Program(argv):
	# Preparation Sector
	argv_lowercase = [x.lower() for x in argv] # Patch Against human captialisation stupidity
	# Sector to check for human errors
	if (not sys.argv[1:]):
		Print_Error ("This program requires arguments in order to function")
		Print_Info ('Refer to: "' + colorama.Fore.YELLOW + sys.argv[0] + ' -h' + colorama.Style.RESET_ALL + ' for a list of valid commands')
		sys.exit(1)
	if (('-h' in argv_lowercase) or ('--help' in argv_lowercase)):
		if (('-d' in argv_lowercase) or ('-c' in argv_lowercase) or ('--compress' in argv_lowercase) or ('--decompress' in argv_lowercase)):
			Print_Error("This option does not take the -d/-c option please check your syntax and try again !")
			Print_Error("Exiting !")
			sys.exit(1)
		help()
		sys.exit(0)
	# Decision Making sector based in specified options
	if (('-c' in argv_lowercase) or ('--compress' in argv_lowercase)):
		if (('-d' in argv_lowercase) or ('--decompress' in argv_lowercase)):
			Print_Error("This option does not take the -d/--decompress option please check your syntax and try again !")
			Print_Error("Exiting !")
			sys.exit(1)
		compress(argv,argv_lowercase)
	if (('-d' in argv_lowercase) or ('--decompress' in argv_lowercase)):
		if (('-c' in argv_lowercase) or ('--compress' in argv_lowercase)):
			Print_Error("This option does not take the -c/--compress option please check your syntax and try again !")
			Print_Error("Exiting !")
			sys.exit(1)
		decompress(argv,argv_lowercase)
	else:
		Print_Error ("Incorrect argument Specified !")
		Print_Info ('Refer to: "' + colorama.Fore.YELLOW + sys.argv[0] + '" -h' + colorama.Style.RESET_ALL + '" for a list of valid commands')
		sys.exit(1)
	return;

def Banner():
	Print_cyan("""

			###             ##              
			 #  ### ### ### # # ### ### ### 
			 #  ##  #   ### # # #   # # # # 
			 #  ### #   # # # # #   ### ### 
			 #              ##          #    

    """)
	Print_Yellow(""" 
	
                            TermDrop By Naix
		========================================
		Codename:           TermDrop
		Made by:            Naix         
		Version:            """ + Version + """
		Language:           Python
		Python Version:     """ + platform.python_version() + """
		Compiler Used:      """ + platform.python_compiler())
	Print_Yellow("""		Operating System:   """ + platform.system() + """""")
	Print_Yellow("""		Hostname:           """ + platform.node() + """""")
	Print_Yellow("""\n""")
	Print_Green("		To go where no binary has gone before.")
	return;

# Main initialization function for easy modification
def Main():
	Banner()
	time.sleep(3)
	Program(sys.argv[1:])
	return;
Main()