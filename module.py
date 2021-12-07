def lists()->list:
	palga=[]
	with open("palga.txt", "r") as f1: #открывает текстовый файл
		for n in f1:
			palga.append(n.strip()) # 
	inimesed=[]
	with open ("inimesed.txt", "r") as inimene:#открывает текстовый файл
		for g in inimene:
			inimesed.append(g.strip())
	return palga,inimesed#возвращает функции

def lisaihmine ():#добавляет сотрудника и зарплату
	name=input("Введите имя - ")
	palga=input("Введите зарплату - ")
	with open("inimesed.txt", "a") as inimesed: #Добавляем человека в конец файла
		inimesed.write(name+"\n")#пишем имя нового сотрудника
	with open("palga.txt", "a") as palga: #Добавляем зарплату в конец файла
		palga.write(palga+"\n")#пишем пароль нового сотрудника

def suurpalk():#Cамая большая зарплата
	palga,inimesed=lists()#Приравниваем к списку
	suurim=max(palga) #Ищем большое число и приравниваем его к переменной
	b=palga.index(suurim) #Приравниваем индекс к переменной для дальнейшего использывания
	print("Самая высокая зарплата у "+inimesed[b]+"palga")

def madalpalk():#Самая маленькая зарплата
	palga,inimesed=lists()
	palgaW=palga.copy()
	palgaW.sort()
	g=palgaW[0]
	h=palga.index(a)
	print("Самая маленькая зарплата у "+inimesed[b]+"зарплата составляет"+ palgadS[0]+"евро")

def keskmine():#вычисляем среднюю зарплату
	palga,inimesed=lists()
	summa=0#сумма равна 0
	for palk in palga:
		summa+=float(palk)#вычисляет зарплату
	kesk=summa/len(palga)#вычислил зарплату
	print("Средняя зарплата"+kesk)
	much=0
	if kesk in palga:
		kesk=inimesed[palga.index(kesk)]
		print(kesk)
	else:
		kesk="lost"
		print(kesk)

def sorteerimine():#Сортировка зарплат и имен
	palgaW=[]
	palga,inimesed=lists()
	palgaW=palga.copy()
	palgaW.sort()
	for palk in palgaW:
		a=palga.index(palk) #Ищем индекс переменной и приравниваем к другой переменной чтобы найти имя и зарплату
		print(palga[a]+" "+inimesed[a])