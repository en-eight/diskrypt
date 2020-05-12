# diskrypt

An open source password encryption tool that uses floppy disks 

Written by Nate Holcomb - nholcom@bgsu.edu

----

### Background

So the background for this was that I was thinking of an offline password 
storage solution that was quick and relatively inaccessible to other people. 
After watching some videos from LGR (Lazy Game Reviews) on Youtube, I saw him 
install drivers from floppy disks and I thought "Hey, nobody really uses those."
What ensued was an idea- encrypt text files and store them on floppy disks. 

And yes, I am dead serious about using floppy disks. They're perfect for holding
text files, being only a couple hundred kilobytes a piece (for huge ones) and 
most people don't have a floppy drive laying around at home. If you do, cool! 
But I don't (for now) and I thought that would be a cool idea to make password
storage more long term rather than in a book or something. It's an automated 
process that's easy to initiate and keep track of. 

I was born in '99, so I have little experience with floppy disks and such. I bet
that they will often fail and they will be slow but for storing text files, eh. 
I want to make this as secure as possible while also making it free for anyone
who wants to use it or adapt it to their own needs. 

I used Python to write all of the code for this program. I intend on extending it
and adding a GUI, hopefully. The encryption algos aren't mine, they are 
pre-established and widely known. 

I hope you enjoy Diskyrpt!

*(this works without floppy disks or any other external storage medium.)*

----

### Command Usage

You need to have Python installed for this to work. Get Python at `https://www.python.org`.

Once Python is installed, start up your command line and change your directory
over to where Diskrypt is stored. For example, on Windows:

`cd C:/Users/myuser/Documents/diskrypt`

Then just run:

`python Diskrypt.py filename.dskp myDecryptKey`

When used properly, you're good to go. Run it again with the same parameters and
it'll decrypt your file and you can actually read your passwords again! If you
run into any errors, see **Error Codes.**

#### Sidenote: `.dskp` files

`.dskp` is my idea for a unique file extension only usable by Diskrypt. The idea
is to make this as inaccessible to others as possible; at the moment it isn't 
particualrly secure or hard to get to. Opening it in Notepad will do the trick.
Text files (`.txt`) are also supported at the moment.

----

### Error Codes

There are a slew of error codes that the program returns. At the moment only four
are implemented. They are as follows"

```python
ARGV_EXCEED = 1				#You passed in too many arguments.
FILE_INVALID = 2			#The file extension is invalid. .txt and .dskp only!
FILE_READ_ERROR = 3			#There was an error reading the file contents.
FILE_WRITE_ERROR = 4		#There was an error writing to the file.
```

The program is set up such that when conditions are met, `sys.exit(ERROR_CODE)`
is thrown and there is another more descriptive error message given by Diskrypt.
As the program is iterated on, I will add more information here as well as any 
troubleshooting steps you can take to fix common errors. 

----

### Bug Reports

If you find any bugs with Diskrypt, feel free to submit an issue on the GitHub
issue page. I will try my absolute best to fix it. I'm not the world's best 
programmer but I will give it an honest go! If you have any suggestions, feel
free to post them there as well. 

----
