# Завдання 1. Аналіз текстового файлу — 2 б.
# Прочитайте файл text.txt. Визначте кількість рядків, слів і символів у всьому файлі. Знайдіть найдовший
# рядок і виведіть його номер, довжину та текст.
# Вимога: файл читати з UTF-8. Порожній символ нового рядка не повинен штучно збільшувати довжину
# найдовшого рядка.
strob = ""
kr = 0 # кількість рядків
ksliv = 0 #кількість слів
ksim = 0 #кількість символів
maxlen = 0 #довжина найдовшого рядка
maxstr = ""  #найдовший рядок
maxks = 0  #номер найдовшого рядка
maxlens = 0 #довжина найдовшого рядка за кількістю слів
maxstrs = ""  #найдовший рядок за кількістю слів
maxkss = 0  #номер найдовшого рядка за кількістю слів
znak = "!;:.,?=+-/*%"
kznak = 0 # кількість знаків (символів)
with open('text.txt', 'r', encoding="utf-8") as file:
    for line in file:
        strob = line.strip()
        ksim = ksim + len(strob)
        #print(strob)
        #print(len(strob))
        s = strob.split()
        kr += 1
        ksliv = ksliv + len(s)
        if maxlen < len(strob):
            maxlen = len(strob)
            maxstr = strob
            maxks = kr

        if maxlens < len(s):
            maxlens = len(s)
            maxstrs = strob
            maxkss = kr

        for char in strob:
            if char in znak:
                kznak = kznak + 1


print(f"Кількість рядків: {kr}")
print(f"Кількість слів: {ksliv}")
print(f"Кількість символів: {ksim}")
print(f"Кількість знаків (символів): {kznak}")

print(f"Найдовший рядок: {maxstr}")
print(f"Номер найдовшого рядка: {maxks}")
print(f"Довжина найдовшого рядка: {maxlen}")

print(f"Найдовший рядок за кількістю слів: {maxstrs}")
print(f"Номер найдовшого за кількістю слів рядка: {maxkss}")
print(f"Довжина найдовшого за кількістю слів рядка: {maxlens}")

# Завдання 2. Пошук фрагмента у файлі — 2 б.
# Користувач вводить фрагмент тексту. Виведіть усі рядки text.txt, у яких він зустрічається, разом із
# номерами рядків. Пошук виконуйте без урахування регістру.
# Якщо збігів немає, виведіть окреме повідомлення.

n = input("Введіть фрагмент: ").lower()
k = 0 # номер рядка \ кількість рядків
kfind = 0 #якщо зустрічаеться
with open('text.txt', 'r', encoding="utf-8") as file2 :
    for line in file2:
        strob = line.strip()
        k += 1
        if n in strob.lower():
            print(f"строка збігу № {k}: {strob}")
            kfind = kfind + 1

if kfind == 0:
    print("Збіг не знайдено.")


# Завдання 3. Результати студентів — 3 б.
# Файл students.txt містить записи у форматі «Прізвище Ім'я;Бал». Прочитайте файл, відберіть студентів з
# балом більше 80, відсортуйте їх за спаданням бала та запишіть результат у result.txt.
# У result.txt кожен студент повинен бути записаний окремим рядком у форматі «Прізвище Ім'я;Бал».
res = []
with open('student.txt', 'r', encoding="utf-8") as file3 :
    for line in file3:
        strob = line.strip()
        s = strob.split(";")

        if int(s[1]) > 80:
            res.append(s)

ress = sorted(res, key=lambda x: x[1], reverse=True) #сортування
print(ress)

with open('result.txt', 'w', encoding="utf-8") as file4 :
    for line in ress:
        file4.write(f"{line[0]};{line[1]}\n")

print(file4)

# Завдання 4. CSV-подібний журнал оцінок — 5 б.
# Файл grades.csv містить записи «name;subject;grade». Один учень може мати кілька записів з різних
# предметів і кілька оцінок з одного предмета. Прочитайте всі записи та сформуйте структуру даних для
# аналізу.
# Для кожного учня обчисліть середній бал за всіма його оцінками. Визначте учня з найвищим середнім
# балом. Сформуйте повний report.txt: ім’я учня, кількість оцінок, середній бал; наприкінці — найкращий
# учень. Учнів у звіті відсортуйте за середнім балом від більшого до меншого.
# Вимога: використовувати split(';'), колекції та функції. Не використовувати pandas. Всі текстові файли —
# UTF-8.

s_stud = [] #кого опрацювали
res_stud = [] #звіт
with open('grades.csv', 'r', encoding="utf-8") as file5:
    lines = file5.readlines()  # зчитуємо всі рядки один раз на початку

    for line in lines:
        strob = line.strip()
        print(strob)
        s = strob.split(";")
        print(s)
        sn = s[0]
        s_so = 0
        sk = 0
        if sn not in s_stud:
            s_stud.append(sn)
            s_so = 0
            sk = 0
            for line1 in lines:
                stro = line1.strip()
                s1 = stro.split(";")
                if s1[0] == sn:
                    s_so = s_so + float(s1[2])
                    sk = sk + 1
            sru = s_so / sk if sk > 0 else 0
            res_stud.append((sn, sk, sru))
resst = sorted(res_stud, key=lambda x: x[1], reverse=True) #сортування
print(resst)

with open('report.txt', 'w', encoding="utf-8") as file6 :
    for line in resst:
        file6.write(f"{line[0]};{line[1]};{line[2]}\n")

print(file6)