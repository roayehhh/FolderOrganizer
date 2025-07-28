import os
import shutil

folderPath = input("1️⃣  Please enter a path: ")

for folder, subfolders, files in os.walk(folderPath):
    for i in files:
        name, ext = os.path.splitext(i)
        ext = ext[1:]
        ext = ext.capitalize()
        sourcePath = os.path.join(folder,i)
        desPath = os.path.join(folder,ext)
        if not os.path.exists(desPath):
            os.mkdir(desPath)
        shutil.move(sourcePath, desPath)
    print("✅ Files moved successfully")