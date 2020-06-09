import ezgmail, os, re

backslash_pattern = r"[\\]" #Regex Pattern to catch all the backslashes in a string
path = r"\credentials.json"

new_path = re.sub(backslash_pattern, "/", path) #We turn all the backslashes(\) into slashes(/) 
print(f"Old Path: {path}\n*New Path: {new_path}")

os.chdir()
ezgmail.init()