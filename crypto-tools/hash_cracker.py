# specifically made for my try hack me task 

import hashlib

wordlist_location = str(input("enter wordlist file location:"))
hash_input = str(input("enter hash to be cracked: "))

with open(wordlist_location, "r") as file:
    for line in file.readlines():
        hash_ob = hashlib.md5(line.strip().encode())
        hased_pass = hash_ob.hexidigest()
        if hashed_pass == hash_input:
            print("found cleartext password!" + line.strip())
            exit(0)