import os
import sys
import main
from shutil import copyfile

def convertFile(filename):
    if filename.endswith('.pdf'):
        cmd = "pdftotext " + filename + " \"/tmp/t2vfile.txt\""
        os.system(cmd)
    elif filename.endswith('.txt'):
        copyfile(filename, "/tmp/t2vfile.txt")
    else:
        print("File format not supported")
        sys.exit()

def start():
    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print("File path does not exist. Exiting...".format(filepath))
	sys.exit()
    convertFile(filepath)
    main.main("/tmp/t2vfile.txt")

start()
