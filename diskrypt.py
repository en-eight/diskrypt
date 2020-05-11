import hashlib
import cogs
from time import datetime
from enum import Enum
import sys

class USERPERFCODES(Enum):
    ENCRYPT_MODE = 1
    DECRYPT_MODE = 2
    QUIT = 3

def main():
    userPref = menu()


    if userPref == ENCRYPT_MODE:
        #this is encryption mode
        #we need to check if there are drives in the right locations.

    elif userPref == DECRYPT_MODE:
        #this is decryption mode.
        #we need to check if there are drives in the right locations.

    else:
        sys.exit(0)