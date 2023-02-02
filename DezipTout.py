"""
Created on Mon Jan  23 2023
Permet l'extraction des fichiers Zip dans un même répertoire. En Python 3.
@author: mcouture
"""
import zipfile,os
basePath = r"Chemin"
os.chdir(basePath)
print(os.curdir)
#Liste des fichiers zip.
listF = os.listdir(os.curdir)

for f in listF:
    if ((f[(len(f)-3):]) == "zip"):
        file_name = os.path.basename(f).replace(".zip", "")
        os.makedirs(file_name)
        zip = zipfile.ZipFile(f)
        print("Extraction de " + f )
        zip.extractall(os.curdir + "/" + file_name)
