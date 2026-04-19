import os

USERNAME = "admin"
PASSWORD = "123"

def login(user,pwd):
    if user == USERNAME and pwd == PASSWORD:
        print("Login successful")
    else:
        print("Login Failed")

def read_file(filename):
    with open(filename, "r") as f:
        print(f.read())

def run_command(cmd):
    os.system(cmd)

if __name__ == "__main__":
    user = input("Username: ")
    pwd = input("Password: ")
    login(user, pwd)

    file = input("Enter filename: ")
    read_file(file)

    cmd = input("Enter command: ")
    run_command(cmd)