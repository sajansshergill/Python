"""
Organize and store your passwords along with the username or the account they are associated with in a text file.
We're not going to store the password in a plain text, we are going to encrypt the passwords.
As we are encrypting, then we might also need a password to decrypt it like there is a master
password for all of the passwords. 
"""

from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) 

def load_key():
    file =  open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'a') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw= data.split("|")
            print("User:", user, "|  Password:", passw, fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue