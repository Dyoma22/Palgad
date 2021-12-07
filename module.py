def lists()->list:
	palgad=[]
	with open("palgad.txt", "r") as f1: #открываем текстовый файл
		for s in f1:
			palgad.append(s.strip()) # 
	inimesed=[]
	with open ("inimesed.txt", "r") as inimene:
		for q in inimene:
			inimesed.append(q.strip())
	return palga,inimesed

def add_person ():
	nimi=input("Введите имя - ")
	palga=input("Введите зарплату - ")
	with open("inimesed.txt", "a") as inimesed: #Добавляем человека в конец файла
		inimesed.write(nimi+"\n")	
	with open("palga.txt", "a") as palgad: #Добавляем зарплату в конец файла
		palgad.write(palga+"\n")

def biggest_salary():
	palga,inimesed=lists()
	suurim=max(palgad) # поиск и прирвынивание самого большого числа к переменной
	b=palga.index(suurim) # приравниваем индекс к переменной для дальнейшего использывания
	print("kõike suured palga on "+inimesed[b]+" palga")

def smallest_salary():
	palgad,inimesed=lists()
	palgadS=palgad.copy()
	palgadS.sort()
	a=palgadS[0]
	b=palgad.index(a)
	print("kõike väiksem palga on "+inimesed[b]+" palga ja see on "+ palgadS[0]+" euro")

def keskmine():#вычисляем среднюю зарплату
	palga,inimesed=lists()
	summa=0
	for palk in palgad:
		summa+=float(palk)
	kesk=summa/len(palga)
	print("keskmine palk "+kesk)
	vahe=0
	if kesk in palga:
		kesk=inimesed[palga.index(kesk)]
		print(kesk)
	else:
		kesk="puudub"
		print(kesk)

def sorting():
	palgaW=[]
	palga,inimesed=lists()
	palgaW=palgad.copy()
	palgaW.sort()
	for palk in palgadS:
		a=palgad.index(palk) # ищем индекс по переменной и приравниваем к другой переменной чтобы найти имя и зарплату в несортированых списках
		print(palga[a]+" "+inimesed[a])