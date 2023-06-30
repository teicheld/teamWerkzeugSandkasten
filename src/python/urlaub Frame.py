import tkinter as tk

def calculate_holiday():
    age = float(age_entry.get())
    disability = float(disability_entry.get())
    seniority = float(seniority_entry.get())

    if age < 18:
        holiday = 30
    elif age >= 55:
        holiday = 28
    else:
        holiday = 26

    if disability >= 50:
        holiday += 5

    if seniority >= 10:
        holiday += 2
    
    result_label.config(text="Sie haben {} Tage Urlaub.".format(holiday))

window = tk.Tk()
window.title("Urlaubsrechner")

age_label = tk.Label(window, text="Wie alt sind Sie?")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

disability_label = tk.Label(window, text="Behinderungsgrad in % (0, falls nicht vorhanden):")
disability_label.pack()
disability_entry = tk.Entry(window)
disability_entry.pack()

seniority_label = tk.Label(window, text="Betriebszugehörigkeit (Jahre):")
seniority_label.pack()
seniority_entry = tk.Entry(window)
seniority_entry.pack()

calculate_button = tk.Button(window, text="Berechnen", command=calculate_holiday)
calculate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()