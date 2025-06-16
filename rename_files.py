import os

dir = input("Enter directory path: ").strip()
print(f"Looking in directory: {dir}")
print(f"Files present: {os.listdir(dir)}")

if not os.path.exists(dir):
    print("Directory not found.")
elif not os.path.isdir(dir):
    print("Path is not a directory.")
elif not os.listdir(dir):
    print("Directory is empty.")
else:
    prefix = input("Enter prefix to add to files: ").strip()
    for file in os.listdir(dir):
        old_file = os.path.join(dir, file)
        new_file = os.path.join(dir, prefix + file)

        os.rename(old_file, new_file)
        print(f"Renamed {file} to {prefix + file}")