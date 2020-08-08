from enum import Enum
import sys


#I do not like this algorithm 
#Maybe change to a Caesar Cipher and then another algo
def encryptStr(userString, userKey):
	return "".join(chr(ord(x) ^ ord(y)) for x,y in zip(userString,userKey))


class ERROR(Enum):
	ARGV_NEQUAL = 1
	FILE_INVALID = 2
	FILE_READ_ERROR = 3
	FILE_WRIT_ERROR = 4
	FILE_DNE = 5

#error check - argv count
if len(sys.argv) != 3:
	print('\n\nUnsuccessful run; the file was not altered. See below:')
	print('''\n\nError! Invalid # of arguments.
	Usage: python ./Diskrypt.py filename.dskp decryption_key\n\n''')
	sys.exit(ERROR.ARGV_NEQUAL)

#Assigning variables from the argument vector.
userFile = sys.argv[1]
userKey = sys.argv[2]

#some part in this process creates artifacts...
if ".dskp" in userFile or ".txt" in userFile and os.path.isfile(userFile) == True:
	with open(userFile, 'r+', encoding="utf-16") as f:
		data = f.read()
		f.seek(0)
		#I'm thinking it's here.
		for l in data:
			f.write(encryptStr(l, userKey))
	f.close
	print("\nSuccessful run. File was altered.\n")
	sys.exit()

else:
	print('\n\nUnsuccessful run; the file was not altered. See below:')
	print('''\n\nError! Invalid file extension.
Accepted file extensions: .dskp .txt\n\n''')
	sys.exit(ERROR.FILE_INVALID)