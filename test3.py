ch1 = int(input("Введите первое число"))
ch2 = int(input("Введите второе число"))
for result in range(ch1, ch2 + 1):
    if result % 2:
        print()
    else:
        print(result + 1)


