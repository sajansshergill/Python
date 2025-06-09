
'''
Write a python program to print the contents of a directory using os module.
Search online for the function which does that.
'''

import os

def list_directory(path='/Users/'):
    try:
        entries = os.listdir(path)
        print(f"Contents of '{path}':")
        for entry in entries:
            print(entry)
    except OSError as e:
        print(f"Error accessing directory '{path}': {e}")

if __name__ == "__main__":
    # replace '.' with your desired directory path
    list_directory('.')
    
    
    
'''
Write a python program to print the contents of a directory using os module.
Search online for the function which does that.


import os

def list_all_files(path='/'):
    for root, dirs, files in os.walk(path):
        for name in files:
            print(os.path.join(root, name))

if __name__ == "__main__":
    list_all_files('/')
'''