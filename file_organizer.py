import os
import shutil

directory = input("Enter directory path to organizee.g. C:/Users/Username/Downloads): ")

if not os.path.exists(directory):
    print("The directory does not exist.")
    exit()

for file in os.listdir(directory):
    file_path = os.path.join(directory, file)

    if os.path.isfile(file_path):
        
        ext = file.split('.')[-1] if '.' in file else 'others'
        
        folder = os.path.join(directory, ext)
        
        if not os.path.exists(folder):
            os.makedirs(folder)
        
        shutil.move(file_path, os.path.join(folder, file))

print("Done organizing files.")

