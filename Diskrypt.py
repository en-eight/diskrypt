import hashlib
from enum import Enum
from itertools import cycle
import sys
import base64

def encryptStr(userString, userKey):
	return "".join(chr(ord(x) ^ ord(y)) for x,y in zip(userString,userKey))


class ERROR(Enum):
	ARGV_NEQUAL = 1
	FILE_INVALID = 2
	FILE_READ_ERROR = 3
	FILE_WRIT_ERROR = 4

if len(sys.argv) != 3:
	print('''\n\nError! Invalid # of arguments.
Usage: python diskryptEncrypt.py filename.dskp decryption_key\n\n''')
	sys.exit(ERROR.ARGV_NEQUAL)

#Assigning variables from the argument vector.
userFile = sys.argv[1]
userKey = sys.argv[2]

if ".dskp" in userFile or ".txt" in userFile:
	with open(userFile, 'r+', encoding="utf-16") as f:
		data = f.read()
		f.seek(0)
		for l in data:
			f.write(encryptStr(l, userKey))

else:
	print('''\n\nError! Invalid file extension.
Accepted file extensions: .dskp .txt\n\n''')
	sys.exit(ERROR.FILE_INVALID)