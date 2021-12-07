from module import*
while True:
	w=input("Функция:\nДобавить сотрудника - 1\nСамая большая зарплата - 2\nСамая маленькая зарплата - 3\nСредняя зарплата - 4\nСортировка - 5")
	if w=="1":
		add_person()
	elif w=="2":
		biggest_salary()
	elif w=="3":
		smallest_salary()
	elif w=="4":
		keskmine()
	elif w=="5":
		sorting()
	else:
		("Этой функций нет")
