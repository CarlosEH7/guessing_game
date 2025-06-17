import os

while True:
    dir = input('Give me a folder: ')


    if not os.path.exists(dir):
        print("Directory does not exists.")
        continue
    else:
        files = os.listdir(dir)
        if not files:
            print("Folder is empty")
            continue
        else:
            for file in files:
                print(f"-{file}")
            print(f"\n")
            break