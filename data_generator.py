#!/usr/bin/python
# Written by - Kartik bhushan


import hashlib

## MD5 function 
def md5_digest(wordlist_file):
	count = 0 
	file = open("md5_digest.txt", "w")
	for i in range(0,len(wordlist_file)):
		file.write(hashlib.md5(wordlist_file[i].replace("\n","").encode()).hexdigest())
		file.write("\n")
		count = count + 1
		print("Progress :: " + str(count) , end="\r")

	print("Total plain text hashesh" + str(len(wordlist_file)))
	print("Total number of hashes written "+ str(count))
	file.close()

## sha1 function 
def sha1_digest(wordlist_file):
	count = 0 
	file = open("sha1_digest.txt", "w")
	for i in range(0,len(wordlist_file)):
		file.write(hashlib.sha1(wordlist_file[i].replace("\n","").encode()).hexdigest())
		file.write("\n")
		count = count + 1
		print("Progress :: " + str(count) , end="\r")

	print("Total plain text hashesh" + str(len(wordlist_file)))
	print("Total number of hashes written "+ str(count))
	file.close()
	
## sha2 function 
def sha256_digest(wordlist_file):
	count = 0 
	file = open("sha256_digest.txt", "w")
	for i in range(0,len(wordlist_file)):
		file.write(hashlib.sha256(wordlist_file[i].replace("\n","").encode()).hexdigest())
		file.write("\n")
		count = count + 1
		print("Progress :: " + str(count) , end="\r")

	print("Total plain text hashesh" + str(len(wordlist_file)))
	print("Total number of hashes written "+ str(count))
	file.close()

if __name__ == "__main__":
	## File read
	wordlist_file = open("rockyou.txt","r" , encoding='cp437').readlines()
	md5_digest(wordlist_file)
	sha1_digest(wordlist_file)
	sha256_digest(wordlist_file)