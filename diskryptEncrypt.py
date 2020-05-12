import hashlib
from enum import Enum
import sys

if len(sys.argv) > 3:
	print('''\n\nError! Too many arguments.
Usage: python diskryptEncrypt.py filename.dskt decryption_key\n\n''')
	sys.exit(0)