from Funktsioonid import *
from palga import *
admin=loe_failist_listisse("adminlogin.txt")#Administraatori kontole sisenemiseks logige sisse
inimesed=loe_failist_listisse("inimesed.txt")#Tavatöötajate sisselogimised
adminpasswords=loe_failist_listisse("passwordadmin.txt")#Parool administraatori kontole sisenemiseks
normpassword=loe_failist_listisse("password.txt")#Parool tavalise konto sisestamiseks 

while True:
	print("Kuhu soovite siseneda?\nKasutaja - [1]\nAdministrator - [2]")
	v=int(input())
	print("Ühendame serveriga\n")
	if v==1:
		print("Kasutaja sisselogimine")
		while 1:
			log=input("Sisesta kasutajanimi:")
			if log in inimesed:
				print("Sisselogimine õige.")
				break
			elif log not in inimesed:
				print("Sisselogimine ei õige.")
		while 1:
			pas=input("Sisestage parool:")
			if pas in normpassword:
				print("Olete sisse logitud, tere tulemast!")
				break
			elif pas not in normpassword:
				print("Vale salasõna")
	elif v==2:
		print("Administraatori sisselogimine.")
		while 1:
			log=input("Sisestage administraatori sisselogimine:")
			if log in admin:
				print("Sisselogimine õige.")
				break
			elif log not in admin:
				print("Sisselogimine ei õige.")
		while 1:
			pas=input("Sisestage parool:")
			if pas in adminpasswords:
				print("Olete sisse logitud, tere tulemast!")
				break
			elif pas not in adminpasswords:
				print("Vale salasõna")
		break
while True:
	print()
	print("Valikud.\nTöötajate nimekiri - [0]\nPalk - [1]\nTipptöötajad - [2]\nTipprikkad ja vaesed - [3]\nKeskmine palk - [4]")
	n=int(input())
	if n==0:
		print()
		print("success")
		print()
		with open("inimesed.txt", "r") as reader:
			print(reader.read())
	elif n==1:
		print()
		print("Success")
		print()
		with open("raha.txt", "r") as reader:
			print(reader.read())
	elif n==2:
		print()
		print("Success")
		print()
		with open("top.txt", "r") as reader:
			print(reader.read())
	elif n==3:
		print()
		print("Success")
		print()
		with open("topfamily.txt", "r") as reader:
			print(reader.read())
	elif n==4:
		print()
		print("Success")
		print()
		with open("topnormal.txt", "r") as reader:
			print(reader.read())
	


