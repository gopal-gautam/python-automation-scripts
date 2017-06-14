from zipfile import ZipFile
import os

def extract(filename, mode, path=os.getcwd(), files_to_extract*):
    if not os.path.exists(filename):
        print "Filename {0} doesnot exists. Exitting...".format(filename)
        return
    zipfile_object = ZipFile(filename)
    if mode=="all":
        zipfile_object.extractall()
        zipfile_object.close()
        return
        
    elif mode=="specific":
        for extract_file_name in files_to_extract:
            zipfile_object.extract(extract_file_name, path=path)
        zipfile_object.close()
        return
            
            