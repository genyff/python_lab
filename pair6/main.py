import tkinter as tk
from tkinter import ttk, scrolledtext
import student_utils
uchni = [
    "Taras",
    "Natalia",
    "Dmytro",
    "Olena",
    "Sasha"
]


def generate_report():
    report_lines = []
    print("=" * 40)
    print("Звіт: ")
    print("=" * 40)

    for name in uchni:
        grades = student_utils.generate_grades(6)
        avg = student_utils.average_grade(grades)
        level = student_utils.get_level(avg)
        grades_str = ", ".join(map(str, grades))
        line = f"Учень: {name}\n  • Оцінки: [{grades_str}]\n  • Середній бал: {avg:.2f}\n  • Рівень: {level.capitalize()}\n"

        report_lines.append(line)
        print(line.strip())
        print("-" * 30)
    full_report = "\n".join(report_lines)
    text_area.config(state=tk.NORMAL)
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, full_report)
    text_area.config(state=tk.DISABLED)



root = tk.Tk()
root.title("Статистика: ")
root.geometry("520x480")
root.minsize(400, 350)

style = ttk.Style()
style.theme_use("clam")

header_label = ttk.Label(root, text="Розрахунок статистики учнів: ", font=("Arial", 14, "bold"))
header_label.pack(pady=12)

btn_generate = ttk.Button(root, text="Показати звіт: ", command=generate_report)
btn_generate.pack(pady=5)

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Consolas", 10))
text_area.pack(padx=15, pady=15, fill=tk.BOTH, expand=True)
text_area.config(state=tk.DISABLED)

root.mainloop()