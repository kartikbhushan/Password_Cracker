import hashlib
from logging.config import valid_ident
from re import S
import colorama
from colorama import Fore , Back 
import time
colorama.init(autoreset=True)

class Cracker:
	def __init__(self, Hashing_Algorithm , Wordlist_file, hash2crack, verbose_flag ):
		self.algo_name = Hashing_Algorithm
		self.Wordlist_file = Wordlist_file
		self.hash2crack = hash2crack
		self.verbose_flag = verbose_flag

	# Switch Statement function
	def algo(self):

		default = "Incorrect Algorithm Name"
		if self.algo_name == "md5":
			return self.md5_digest()
		elif self.algo_name == "sha1":
			return self.sha1_digest()
		elif self.algo_name == "sha256":
			return self.sha256_digest()
		else:
			print(default)
 
	# def md5_hash(self):
	def md5_digest(self):
		for i in range(0,len(self.Wordlist_file)):
			self.hash2comp = hashlib.md5(self.Wordlist_file[i].replace("\n","").encode()).hexdigest()

			# just display fun - Can be muted if needed
			if int(verbose_flag) == 1:
				print(Fore.RED + " Word - " + Fore.WHITE +  self.Wordlist_file[i].replace("\n" , "") + Fore.RED + " Hash - " + Fore.WHITE + self.hash2comp + Fore.RED + " Password_hash - " + Fore.WHITE + self.hash2crack)
				if self.hash2crack == self.hash2comp:
					return self.Wordlist_file[i].replace("\n" , "")

			elif int(verbose_flag) ==  0:
				if self.hash2crack == self.hash2comp:
					return self.Wordlist_file[i].replace("\n" , "")
			else:
				return Fore.RED + "Password not found"

	def sha1_digest(self):
		for i in range(0,len(self.Wordlist_file)):
			self.hash2comp = hashlib.sha1(self.Wordlist_file[i].replace("\n","").encode()).hexdigest()

			# just display fun - Can be muted if needed
			if int(verbose_flag) == 1:
				print(Fore.RED + " Word - " + Fore.WHITE +  self.Wordlist_file[i].replace("\n" , "") + Fore.RED + " Hash - " + Fore.WHITE + self.hash2comp + Fore.RED + " Password_hash - " + Fore.WHITE + self.hash2crack)
				if self.hash2crack == self.hash2comp:
					return self.Wordlist_file[i].replace("\n" , "")

			elif int(verbose_flag) ==  0:
				if self.hash2crack == self.hash2comp:
					return self.Wordlist_file[i].replace("\n" , "")
			else:
				return Fore.RED + "Password not found"
	
	
	# SHA 256 Algorithm
	def sha256_digest(self):
		for i in range(0,len(self.Wordlist_file)):
			self.hash2comp = hashlib.sha256(self.Wordlist_file[i].replace("\n","").encode()).hexdigest()

			# just display fun - Can be muted if needed
			if int(verbose_flag) == 1:
				print(Fore.RED + " Word - " + Fore.WHITE +  self.Wordlist_file[i].replace("\n" , "") + Fore.RED + " Hash - " + Fore.WHITE + self.hash2comp + Fore.RED + " Password_hash - " + Fore.WHITE + self.hash2crack)
				if self.hash2crack == self.hash2comp:
					return self.Wordlist_file[i].replace("\n" , "")

			elif int(verbose_flag) ==  0:
				if self.hash2crack == self.hash2comp:
					return self.Wordlist_file[i].replace("\n" , "")
			else:
				return Fore.RED + "Password not found"

	


if __name__ == "__main__":
	## File inputs 
	Wordlist = input("Wordlist : ")
	hash2crack = input("Hash: ")
	Hashing_Algorithm = input("Algorithm :")
	verbose_flag = input("Verbose Output (1/0) :")

	# Read files 
	Wordlist_file = open(Wordlist , "r" , encoding='cp437').readlines()
	
	# Class object - Cracker
	cracker = Cracker(Hashing_Algorithm , Wordlist_file, hash2crack,verbose_flag)
	st = time.time()
	print(f"{Fore.GREEN}Cracked Password is = {Fore.RED}{Back.WHITE}{cracker.algo()}")
	et = time.time()
	elapsed_time = et-st 
	print("Execution time:"+  time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))