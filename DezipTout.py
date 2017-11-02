# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 09:24:06 2017
Permet l'extraction des fichiers Zip dans un même répertoire. En Ptyhon 3.
@author: mcouture
"""
import zipfile,os

print (os.curdir)
#Liste des fichiers zip. 
listF = os.listdir(os.curdir)

for f in listF:
    if ((f[(len(f)-3):]) == "zip"):
        zip = zipfile.ZipFile(f)
        print("Extraction de " + f )
        zip.extractall(os.curdir)