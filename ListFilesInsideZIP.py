from zipfile import ZipFile
import os
import sys

if len(sys.argv) < 1:
    print "No filename specified here. Exiting..."
    sys.exit()
filepath = sys.argv[1]
if not os.path.exists(filepath):
    print "filepath {0} doesnot exist".format(filepath)
    sys.exit()
zipfile_object = ZipFile(filepath)
zipfile_object.printdir()
zipfile_object.close()