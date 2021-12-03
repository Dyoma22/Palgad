from Funktsioonid import *
from palga import *
import time
Admin=loe_failist_listisse("adminlogin.txt")#Логин для входа в админ аккаунт
Inimesed=loe_failist_listisse("inimesed.txt")#Логины для обычного персонала
APasswords=loe_failist_listisse("passwordadmin.txt")#Пароль для входа в админ аккаунт
Passwords=loe_failist_listisse("password.txt")#Пароль для входа в обычный аккаунт 

while True:
	print("Куда хотите войти?\nПользоватьель-[0]\nАдминистратор-[1]")
	v=int(input())
	print("Идет вход...\n")
	print("Синхронизация данных...\n")
	if v==0:
		print("Вход Пользователя...")
		while 1:
			log=input("Введите логин:")
			if log in Inimesed:
				print("Логин успешно введён.")
				break
			elif log not in Inimesed:
				print("Не верный логин.")
		while 1:
			pas=input("Введите пароль:")
			if pas in Passwords:
				print("Вы вошли в систему.")
				break
			elif pas not in Passwords:
				print("Не верный пароль.")
	elif v==1:#вход как админ
		print("Вход Администрации...")
		while 1:
			log=input("Введите логин:")#Писать Sergei, другое не примит
			if log in Admin:
				print("Логин успешно введён.")
				break
			elif log not in Admin:
				print("Не верный логин.")
		while 1:
			pas=input("Введите пароль:")#Пароль 7493
			if pas in APasswords:
				print("Вы вошли в систему.")
				break
			elif pas not in APasswords:
				print("Не верный пароль.")
		break
while True:
	print("Что хотите посмотреть?\nCписок сотрудников-[0]\nЗарплата-[1]\nТоп сотрудников-[2]")
	n=int(input())
	print("Загрузка...")
	if n==0:
		print("Вход в список сотрудников...")
		with open("inimesed.txt", "r") as reader:#Читает содержимое файла и выводим на экран
			print(reader.read())
	elif n==1:
		print("Вход в систему зарплаты...")
		with open("raha.txt", "r") as reader:
			print(reader.read())
	elif n==2:
		print("Вход в топ сотрудников...")
		with open("top.txt", "r") as reader:
			print(reader.read())