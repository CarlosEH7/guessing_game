import hashlib
from difflib import SequenceMatcher

def hash_file(fileName):
    
    #Use hashlib to store the hash of a file
    h = hashlib.sha1()

    with open(fileName, "rb") as file:

        #Use file.read() to read the size of file
        #and read the file in small chunks
        # because we cannot read the large files
        chunk = file.read(1024)
        while chunk != b'':
            h.update(chunk)
            chunk = file.read(1024)
        return h.hexdigest()

file1 = input("Enter the first file name ").strip()
file2 = input("Enter the second file name ").strip()

try:
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)
    
    if(file1 != file2):
        print("These files are not identical")
    else:
        print("These files are identical")
except FileNotFoundError as e:
    print(f"File error: {e}")
