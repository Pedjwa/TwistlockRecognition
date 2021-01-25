import PIL
import os
import os.path
from PIL import Image

def BulkRename(fotoDir):
    os.chdir(fotoDir)
    objectName = "Test"
    nameList = os.listdir()
    for fileNr in range(len(nameList)):
        try:
            rename=(objectName + " " + str(fileNr) + ".JPG")
            os.rename(nameList[fileNr],rename)
            print("File ", nameList[fileNr], "renamed to ", rename)
        except:
            print("Exception Thrown")
				
				
fotoDir = (".\Test\\")
BulkRename(fotoDir)