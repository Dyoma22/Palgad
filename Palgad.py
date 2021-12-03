from Funktsioonid import *
from palga import *
admin=loe_failist_listisse("adminlogin.txt")#Administraatori kontole sisenemiseks logige sisse
inimesed=loe_failist_listisse("inimesed.txt")#Tavatöötajate sisselogimised
adminpasswords=loe_failist_listisse("passwordadmin.txt")#Parool administraatori kontole sisenemiseks
normpassword=loe_failist_listisse("password.txt")#Parool tavalise konto sisestamiseks 

while True:#lõputu tsükkel kuni toimingu sooritamiseni või kuni selle lõpuni
	print("Kuhu soovite siseneda?\nKasutaja - [1]\nAdministrator - [2]")#kirjutab teksti ja pakub valida administraatori või kasutaja
	v=int(input())#peamine märk
	print("Ühendame serveriga\n")#kirjutab teksti
	if v==1:#Logi sisse töötajana
		print("Kasutaja sisselogimine")#kirjutab teksti
		while 1:
			log=input("Sisesta kasutajanimi:")#kirjutab tekssti ja küsib sisselogimist
			if log in inimesed:#kui sisselogimine on tekstifailis, siis on kõik edukas
				print("Sisselogimine õige.")#kui kõik on ok, siis kirjuta, mis on õige
				break#katkestab tsükli
			elif log not in inimesed:#kui nimekirjas pole sisselogimist, ütleb ta, et sellist sisselogimist pole
				print("Sisselogimine ei õige.")#kirjutab teksti
		while 1:
			pas=input("Sisestage parool:")
			if pas in normpassword:
				print("Olete sisse logitud, tere tulemast!")#kirjutab teksti ja kui parool on tekstifailis, jäetakse see vahele
				break
			elif pas not in normpassword:#kirjutab tektsi ja kui parooli pole, ei lähe see läbi
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
	


