# Задание первое
print('Введите четыре профессии:' "\nКто он?")
profa = input('Первая профессия')
profb = input('Вторая профессия')
profc = input('Третья профессия')
print("Кто он?" "\nОн -"" " + profa + " " "и" " " + profb + " " "и" " " + profc + ".")


# Задание второе
print("Сейчас мы переведём ваши минуты в 'часы и минуты!'")
a = int(input("Введите количество минут: "))
b = a // 60  # Узнаём сколько часов в минутах, введённых пользователем.
d = a % 60  # Узнаём сколько минут с помощбю деления по модулю.
print(str(b) + " " "час." " " "и" " " + str(d) +" " "мин.")