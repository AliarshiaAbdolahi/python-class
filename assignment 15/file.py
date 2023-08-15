import os
import shutil

CWD = os.getcwd()
Files = os.listdir()
Path = CWD + "\images"
Pas_files = ["jpeg", "jpg", "png", "gif"]

if "images" not in Files:
    os.mkdir(Path)

for i in Files:
    if "." in i:
        for j in Pas_files:
            if i.split(".")[1] == j:
                shutil.copy(i, Path)