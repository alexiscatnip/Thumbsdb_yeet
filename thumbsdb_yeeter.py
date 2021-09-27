# deletes all files called Thumbs.db that exists inside the specified root folder. recursive.
# First argument is the root folder.

#usage example:
#  python thumbsdb_yeeter.py D:\images

import sys
from pathlib import Path
import os

def recursive_yeet(dir_path, dry_run):
    try:
        for entry in os.scandir(dir_path):
            if entry.is_dir():
                recursive_yeet(entry.path, dry_run)
            if ( entry.is_file() and (entry.name == "Thumbs.db") ):
                    if(dry_run):
                        print_file_entry(entry)
                    else:
                        yeet(entry)
    except:
        return #catches access is denied

def yeet(file):
    try:
        os.remove(file.path) 
    except OSError:
        print("Failed to yeet      " + file.name + " at " + file.path)
        pass
    else:
        print("Successfully yeeted " + file.name + " at " + file.path)
        
def print_file_entry(file):
    print("Found        " + file.name + " at " + file.path)
    
if __name__ == '__main__':
    if (len(sys.argv) != 2):
        raise RuntimeError("bad args")
    
    root_dir_str = sys.argv[1]
    root_dir = Path(root_dir_str)
    if (not root_dir.exists()):
        raise RuntimeError("root folder not exist")

    recursive_yeet(root_dir, True)
    print ("+++++++++++++++++++++++++")
    _in = input("do you wish to yeet the above files? y/n ")
    print ("+++++++++++++++++++++++++")
    if (_in == "y"):
        recursive_yeet(root_dir, False)
        print ("done yeeting.")
    else:
        print ("no yeeting today.")