import socket
import requests
import json
import threading
import tldextract
from multiprocessing.dummy import Pool as ThreadPool

# Preparing result list
try:
	ipresults = open("result-lists.txt", "x")
except:
	pass
class reversing:
	def __init__(self,target, domains):
		self.target = target
		self.domains = domains

	# Get response result from sonar omnisint
	def getreverse(self):
		req = requests.get("https://sonar.omnisint.io/reverse/" + self.target)
		loadres = json.loads(req.text)
		if int(menus)==2:
			for i in loadres:
				self.checkduplicates(i)
		else:
			print(str(self.domains) +  " || Total : " + str(len(loadres)))
			for i in loadres:
				self.checkduplicate(i)
	#checking on by one if duplicates & if there's subdomain
	def checkduplicates(self, domainres):
		loadlist = open("result-lists.txt", "r").read().split("\n")
		tocheckz = tldextract.extract(domainres)
		if domainres in loadlist:
			print("[!Duplicates] " + domainres + " Deleting.....")
		if tocheckz.subdomain != "" and tocheckz.subdomain !="www":
			print("[!Subdo] " + domainres)
		else:
			print("[VALID] " + str(domainres))
			with open("result-lists.txt", "a") as newwrite:
				newwrite.write(str(domainres) + "\n")
	def checkduplicate(self, domainres):
		with open("result-lists.txt", "a") as newwrite:
			newwrite.write(str(domainres) + "\n")

def revip(inp):
	getip = socket.gethostbyname(inp)
	loadtrash = open("result-lists.txt", "r").read().split("\n")
	if getip in loadtrash:
		print("[!] " + str(getip) + " == Duplicates")
	else:
		print(getip)
		revip = reversing(getip, inp)
		revip.getreverse()

def main():
	print("|==========================|")
	print("*    Reverse ip    *")
	print("*    https://github.com/shizuocode/reverse-ip")
	print("|==========================|\n")
	print("1. Reverse ip + Subdomain")
	print("2. Reverse ip & Delete subdomains\n")
	global menus
	menus = input("~#Choose : ")
	targetlist = open(input("~#Input list : "), "r").read().replace("https://", "").replace("http://", "").replace("/", "").split("\n")
	Thread = input("~#Thread : ")
	pool = ThreadPool(int(Thread))
	pool.map(revip,targetlist)
	pool.close()
	pool.join()
if __name__ == '__main__':
	main()