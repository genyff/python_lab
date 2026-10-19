# Завдання 1. Аналіз і фільтрація списку — 2 б.
# Дано список чисел. Сформуйте окремі списки додатних, від’ємних, парних та чисел, кратних 3. Для
# початкового списку знайдіть мінімальне, максимальне значення, суму та середнє арифметичне.
# Вимога: нові списки формувати циклом і append(). Не змінювати початковий список.
n = [12, 3, 4, 14, -12, 5, 10, 16, -4]
nd = [] #список доданих
nv = [] #список від'ємних
np = [] #список парних
nk3 = [] #числа кратні на 3
nm = n[0]#мінімальне
nmax = n[0] #максимальне
nsum = 0
nsru = 0 #середнє арифметичне
k = 0
for num in n:
    if num > nmax:
        nmax = num
    if num < nm:
        nm = num
    if num < 0:
        nv.append(num)
    if num > 0:
        nd.append(num)
    if num % 2 == 0:
        np.append(num)
    if num % 3 == 0:
        nk3.append(num)
    nsum += num
    k = k + 1
nsru = nsum / k
print("середнє арифметичне: ", nsru)
print("список доданих: ", nd)
print("список від'ємних: ", nv)
print("список парних: ", np)
print("числа кратні на 3: ", nk3)
print("мінімальне: ", nm)
print("максимальне: ", nmax)
print("сума: ", nsum)


# Завдання 2. Дві групи учасників — 2 б.
# Створіть два набори імен учасників за допомогою set. Визначте учасників, які є в обох групах; тільки в
# першій; тільки в другій; а також усіх унікальних учасників.
# Вимога: використати операції множин, а не вкладені цикли.
group1 = {'Anna','Ivan','Olha'}
group2 = {'Ivan','Maksym','Olha'}
setog = set()
setog = group1 & group2 #& перетин
setfirst = group1 - group2 #- різниця
setsecond = group2 - group1
uni = group1 | group2 #| об'єднання
print(f"Спільні: {setog}")
print(f"Тільки group1: {setfirst}")
print(f"Тільки group2: {setsecond}")
print(f"Усі: {uni}")


# Завдання 3. Каталог товарів — 3 б.
# Створіть словник товарів, де ключ — назва товару, значення — ціна. Реалізуйте додавання нового товару
# або зміну ціни існуючого, пошук товару за назвою та виведення всіх товарів у заданому користувачем
# ціновому діапазоні.
# Вимога: використати get() для безпечного пошуку та items() для перебору каталогу.
#
# ct каталог товарів
ct  = {
    "bread": 25,
    "milk": 48,
    "tea": 75,
    "apple": 30
}
minp = 40
maxp = 100
print(f"вхідні дані, ціновий діапазон: {minp}..{maxp} грн")
print("результат")
for name, price in ct.items():
    if minp <= price <= maxp:
        print(f"{name} - {price}")
item = "milk"
p = ct.get(item)

# Завдання 4. Журнал групи — 5 б.
# Створіть програму «Журнал групи». Дані учнів зберігайте у словнику: ключ — ПІБ, значення — список із
# 5 оцінок. Реалізуйте додавання учня, друк усього журналу, середній бал кожного учня, рейтинг учнів за
# середнім балом та пошук учня з найвищим середнім балом.
# Незмінні дані групи (наприклад, назва групи та навчальний рік) збережіть у tuple. Перевіряйте, що кожен
# учень має рівно 5 оцінок у діапазоні 1–12.
naz = input("Введіть назву групи: ")
rik = input("Введіть навчальний рік: ")
nazrik = (naz, rik)
diap = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"}
slowuch = {}
t = True
while t == True:
    pib = input("Введіть ПІБ учня, або enter для завершення вводу: ")
    if pib == "":
        break
    else:
        ocin = input("Введіть 5 оцінок від 1 до 12 через кому: ")
        ocinka = ocin.split(",")
        print(len(ocinka))
        if len(ocinka) != 5:
            print("Увага! Потрібно ввести 5 оцінок від 1 до 12 через кому. Ваш ввод не зараховано. Повторіть. ")
        else:
            t = False
            numocin = []
            for oc in ocinka:
                if oc not in diap:
                    t = True
                    print("Увага! Потрібно ввести 5 оцінок від 1 до 12 через кому. Ваш ввод не зараховано. Повторіть. ")
                else:
                    numocin.append(int(oc))
            if t == False:
                slowuch[pib] = numocin
                t= True

print(slowuch)
print(f"\nЖурнал групи {nazrik[0]}. Навчальний рік: {nazrik[1]} ")

if not slowuch:
    print("Журнал порожній.")
else:
    print("\nДрук журналу та середній бал кожного учня:")
    for pib, ocinka in slowuch.items():
        sru = sum(ocinka) / len(ocinka)
        print(f"{pib}: {ocinka} | Середній бал: {sru:.2f}")

    print("\nЖурнал рейтингу учнів")
    sortuch = sorted(
        slowuch.items(),
        key=lambda item: sum(item[1]) / 5,
        reverse=True
    )
    for i, (pib, ocinka) in enumerate(sortuch, start=1):
        sru = sum(ocinka) / 5
        print(f"{i}. {pib} — середній бал: {sru:.2f}")

    naiuch = max(slowuch, key=lambda pib: sum(slowuch[pib]) / len(slowuch[pib]))
    naisru = sum(slowuch[naiuch]) / 5
    print(f"\nНайвищий середній бал у учня: {naiuch} ({naisru:.2f})")





