import math
import statistics as stat
from math import *
import random
import demo
from tkinter import *
from datetime import datetime


# print(math.sqrt(81))
# a = [10, 15, 8, 9]
# print(f'Середній бал: {stat.mean(a)}')
# r = int(input("r = "))
# circle_area = round(pi * pow(r, 2))
#
#
# print(circle_area)

# balls = 25
# n = 6
# print(f'повністю заповнених коробок: {floor(balls/n)}')
# print(f'всього коробок: {ceil(balls/n)}')

# numbers = []
# for i in range(10):
#     numbers.append(random.randint(1,100))
# print(f'випадкові 10 чисел: {numbers}')
#
# selected = random.choice(numbers)
# print(f'Випадкове число із послідовністю: {selected}')
# print(f'сьогодні: {date.today()}')

# print(demo.square(5))
# print(demo.is_even(7))
# grades = [12,5,7,9]
# print(demo.average(grades))
#

window = Tk()
window.title('my first window')
window.geometry('500x400')
window.mainloop()
window.resizable(False, False)
window["bg"] = "#F19CBB"
frame = Frame(window)

frame.pack()
bt1 = Button(frame, text = "OK")
bt1.grid(row = 0, column = 0)
bt2 = Button(frame, text = "Cancel")
bt2.grid(row = 0, column = 1)
label = Label(window, text="ne", font=("Arial, 18"), bg="#F19CBB")
# label.place(x = 0, y = 0)
label.pack()


















