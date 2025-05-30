import os
import re

folder_path = rf"pathhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"

if not os.path.exists(folder_path):
    print(f" Not exist: {folder_path}")
    exit()

pattern = re.compile(r"what you want to delete")

for filename in os.listdir(folder_path):
    old_path = os.path.join(folder_path, filename)

    if os.path.isfile(old_path):
        new_name = pattern.sub("", filename).strip()  
        new_path = os.path.join(folder_path, new_name)

        if filename != new_name:
            try:
                os.rename(old_path, new_path)
                print(f" renamed: {filename} → {new_name}")
            except Exception as e:
                print(f" error {filename}: {e}")

print(" Done ")
